import os
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import torch
import torch.nn.functional as F
from torchvision import transforms
from transformers import ViTFeatureExtractor, ViTModel


# Define Image Loading and Preprocessing Functions
def load_image(image_path):
    """Load an image from the specified path."""
    return Image.open(image_path).convert('RGB')

def preprocess_image(image, image_size=224):
    """Preprocess the image for the Vision Transformer."""
    preprocess = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return preprocess(image).unsqueeze(0)  # Add batch dimension


# Load Pretrained Vision Transformer Model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model_repo = 'google/vit-base-patch16-224'
feature_extractor = ViTFeatureExtractor.from_pretrained(model_repo)
vit_model = ViTModel.from_pretrained(model_repo).to(device)
vit_model.eval()


# Define Similarity Metrics
## Cosine Similarity Using ViT Embeddings
def get_vit_embedding(image_path, model, device):
    """Compute the Vision Transformer embedding for an image."""
    image = load_image(image_path)
    image = preprocess_image(image).to(device)
    with torch.no_grad():
        outputs = model(image)
    return outputs.last_hidden_state[:, 0, :]  # CLS token embedding


def cosine_similarity(embeddingA, embeddingB):
    """Compute the cosine similarity between two embeddings."""
    return F.cosine_similarity(embeddingA, embeddingB).item()


## Structural Similarity Index (SSIM)
def calculate_ssim(imageA_path, imageB_path):
    """Compute the Structural Similarity Index between two images."""
    imageA = np.array(load_image(imageA_path).convert('L'))
    imageB = np.array(load_image(imageB_path).convert('L'))
    return ssim(imageA, imageB)


# Compare Images Using Multiple Metrics
def compare_images(original_image_path, embedded_image_path, model, device):
    """Compare two images using various similarity metrics."""
    # Compute ViT embeddings
    orig_embedding = get_vit_embedding(original_image_path, model, device)
    emb_embedding = get_vit_embedding(embedded_image_path, model, device)
    vit_cosine_sim = cosine_similarity(orig_embedding, emb_embedding)

    # Compute SSIM
    ssim_index = calculate_ssim(original_image_path, embedded_image_path)

    # Print results
    print(f"ViT Cosine Similarity: {vit_cosine_sim:.4f}")
    print(f"SSIM: {ssim_index:.4f}")


# Process a Dataset of Image Pairs
def process_image_pairs(original_dir, embedded_dir, model, device):
    """Process and compare pairs of images from the specified directories."""
    original_images = sorted(os.listdir(original_dir))
    embedded_images = sorted(os.listdir(embedded_dir))

    # Debugging: Print out file lists
    print("Original Images:", original_images)
    print("Embedded Images:", embedded_images)

    for orig_img in original_images:
        orig_path = os.path.join(original_dir, orig_img)

        # Construct the expected reconstructed filename
        base_name, ext = os.path.splitext(orig_img)
        rec_img = f"{base_name}_rec{ext}"
        emb_path = os.path.join(embedded_dir, rec_img)

        # Check if reconstructed image exists
        if not os.path.exists(emb_path):
            print(f"Skipping {orig_img}: No matching {rec_img} found.")
            continue

        print(f"Comparing {orig_img} and {rec_img}:")
        compare_images(orig_path, emb_path, model, device)
        print('-' * 50)


# Main Execution
if __name__ == '__ main __':
    original_images_dir = 'images/original'
    embedded_images_dir = 'images/embedded'
    process_image_pairs(original_images_dir, embedded_images_dir, vit_model, device)
