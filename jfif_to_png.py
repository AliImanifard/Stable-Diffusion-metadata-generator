from PIL import Image
import os

# Input and output directories
input_dir = "images"
output_dir = "images_png"

### I created the following codes, that is, the following folders,
### so that I could reproduce images that were not 512*768 and convert them back to PNG.
#input_dir = "images_jfif_new512in768"  # Replace with your input directory
#output_dir = "images_png_new512in768"  # Replace with your output directory

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".jfif"):
        # Open the image file
        img_path = os.path.join(input_dir, filename)
        image = Image.open(img_path)

        # Create output path with .png extension
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_dir, output_filename)

        # Convert and save as PNG
        image.save(output_path, "PNG")
        print(f"Converted: {filename} -> {output_filename}")

print("Conversion completed!")