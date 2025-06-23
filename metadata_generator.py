import os
import random
from faker import Faker
from datetime import datetime, timedelta
from PIL import Image  # To extract image dimensions

# Initialize Faker
fake = Faker()

# Define the directory containing images
image_dir = "images/original"  # The folder where the images are located.
output_dir = "metadata_files"  # A folder to store metadata files.

### I created the following codes, that is, the following folders,
### so that I could reproduce metadata for the images that were not 512*768.
#image_dir = "images_png_new512in768"
#output_dir = "metadata_files_for_png_images_new512in768"  # A folder to store metadata files.



os.makedirs(output_dir, exist_ok=True)

# Define a list of possible values for some fields
operating_systems = ["Windows 10", "Windows 11", "macOS Catalina", "Ubuntu 20.04"]
class_names = ["Art 101", "Computer Science 101", "Mathematics 101",
               "Art 102", "Computer Science 102", "Mathematics 102",
               "Art 103", "Computer Science 103", "Mathematics 103",
               "Art 104", "Computer Science 104", "Mathematics 104",
               "Art 105", "Computer Science 105", "Mathematics 105"]
course_codes = ["ART101", "CS101", "MATH101"]
professor_names = ["Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Davis", "Dr. Wilson",
                   "Dr. Miller", "Dr. Anderson", "Dr. Taylor", "Dr. Thomas", "Dr. Jackson",
                   "Dr. White", "Dr. Harris", "Dr. Martin", "Dr. Thompson", "Dr. Garcia",
                   "Dr. Martinez", "Dr. Robinson", "Dr. Clark", "Dr. Rodriguez", "Dr. Lewis"]

semesters = ["Fall", "Spring", "Summer"]
academic_years = ["2022-2023", "2023-2024", "2024-2025"]
software_names = ["Krita", "Photoshop", "GIMP"]
ai_models = ["Stable Diffusion"]
ai_providers = ["Stability AI"]
sampling_methods = ["Euler a", "DDIM", "PLMS"]

# Define prompt intervals and their corresponding prompts and negative prompts
prompt_intervals = [
    {
        "start": 1,  # Start of interval
        "end": 6,  # End of interval
        "prompt": "Goal: Basic sketches and shading. Create a detailed pencil sketch of an apple, including shading "
                  "to show its round shape and a highlight on the top-right side.",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 7,
        "end": 9,
        "prompt": "Goal: Basic sketches and shading. Create a detailed pencil sketch of an pineapple with no color, "
                  "including shading to show its round shape and a highlight on the top-right side.",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 10,
        "end": 15,
        "prompt": "((black and white pencil drawing)), Draw a front-view pencil sketch of a human face, focusing on "
                  "proportions: eyes, nose, mouth, and ears. Include light shading to define the facial structure. "
                  "Goal: Basic sketches and shading., black and white, breathtaking pencil illustration, "
                  "highly detailed, 4k, (textured paper), pencil texture, sketch",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 16,
        "end": 21,
        "prompt": "((black and white pencil drawing)), Generate a pencil sketch of a sitting cat, focusing on fur "
                  "texture and proportions. Include shading to show the light source from the top-left. Goal: Basic "
                  "sketches and shading. , black and white, breathtaking pencil illustration, highly detailed, 4k, "
                  "(textured paper), pencil texture, sketch",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 22,
        "end": 27,
        "prompt": "((black and white pencil drawing)), Generate a pencil sketch of a library with five people: two "
                  "sitting at a table, one standing by a bookshelf, and two walking in the background. Goal: Train to "
                  "generate complex, crowded scenes. , black and white, breathtaking pencil illustration, "
                  "highly detailed, 4k, (textured paper), pencil texture, sketch",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 28,
        "end": 29,
        "prompt": "Create a detailed colored pencil drawing of a fruit, including color.",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 30,
        "end": 31,
        "prompt": "Create a detailed colored pencil drawing of a face with no detail, including color",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 32,
        "end": 33,
        "prompt": "Create a detailed colored pencil drawing of a face with a lot of details including color and "
                  "focusing on proportions: eyes, nose, mouth, and ears. Include light shading to define the facial "
                  "structure,",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 34,
        "end": 35,
        "prompt": "Create a detailed colored pencil drawing of an animal including color.",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 36,
        "end": 37,
        "prompt": "Generate a colored pencil of a small section of a library, featuring two people sitting at a table "
                  "and one person walking by. Include bookshelves in the background.",
        "negative_prompt": "stationary, holding pen, holding paper, low-quality, deformed, photo, 3D render, text, "
                           "poorly drawn"
    },
    {
        "start": 38,
        "end": 39,
        "prompt": "Generate a charcoal drawing of a simple still life: a bowl with two apples inside. Use bold, "
                  "dark strokes for shadows and soft strokes for highlights.",
        "negative_prompt": "NULL"
    },
    {
        "start": 40,
        "end": 41,
        "prompt": "Create a charcoal drawing of a face with no detail.",
        "negative_prompt": "NULL"
    },
    {
        "start": 42,
        "end": 42,
        "prompt": "Create a detailed charcoal drawing drawing of a face with a lot of details focusing on "
                  "proportions: eyes, nose, mouth, and ears. Include light shading to define the facial structure.",
        "negative_prompt": "NULL"
    },
    {
        "start": 43,
        "end": 44,
        "prompt": "Create a detailed charcoal drawing drawing of an animal.",
        "negative_prompt": "NULL"
    },
    {
        "start": 45,
        "end": 48,
        "prompt": "Create a detailed charcoal sketch of a library scene, adding facial expressions, clothing details, "
                  "and interactions between people.",
        "negative_prompt": "NULL"
    },
    {
        "start": 49,
        "end": 54,
        "prompt": "Generate a watercolor drawing of a simple still life: a bowl with two apples inside. Use bold, "
                  "dark strokes for shadows and soft strokes for highlights., (watercolor), high resolution, "
                  "intricate details, 4k, wallpaper, concept art, watercolor on textured paper",
        "negative_prompt": "low-quality, deformed, text, poorly drawn"
    },
    {
        "start": 55,
        "end": 60,
        "prompt": "Create a watercolor drawing of a face with no detail., (watercolor), high resolution, intricate "
                  "details, 4k, wallpaper, concept art, watercolor on textured paper",
        "negative_prompt": "low-quality, deformed, text, poorly drawn"
    },
    {
        "start": 61,
        "end": 62,
        "prompt": "Create a detailed watercolor drawing drawing of a face with a lot of details focusing on "
                  "proportions: eyes, nose, mouth, and ears. Include light shading to define the facial structure. , "
                  "(watercolor), high resolution, intricate details, 4k, wallpaper, concept art, watercolor on "
                  "textured paper.",
        "negative_prompt": "low-quality, deformed, text, poorly drawn"
    },
    {
        "start": 63,
        "end": 65,
        "prompt": "Create a detailed watercolor drawing of an animal with jungle background., (watercolor), "
                  "high resolution, intricate details, 4k, wallpaper, concept art, watercolor on textured paper.",
        "negative_prompt": "low-quality, deformed, text, poorly drawn"
    },
    {
        "start": 66,
        "end": 67,
        "prompt": "Create a detailed watercolor drawing of a library scene, adding facial expressions, clothing "
                  "details, and interactions between people., (watercolor), high resolution, intricate details, 4k, "
                  "wallpaper, concept art, watercolor on textured paper ",
        "negative_prompt": "low-quality, deformed, text, poorly drawn"
    },
    {
        "start": 68,
        "end": 70,
        "prompt": "(Create an oil painting of a ripe orange fruit, including its texture and a highlight on the "
                  "top-right. Use warm colors for the fruit and a neutral background.) (Oil painting) (by "
                  "Jean-François Millet), (by Gustave Courbet), (by Jules Breton), close up",
        "negative_prompt": "frame, (badly drawn hands), extra limbs, extra fingers, bad anatomy"
    },
    {
        "start": 71,
        "end": 72,
        "prompt": "breathtaking alla prima oil painting, Create an oil painting of a simple in front view human face "
                  "with fully clothes and in no detail., close up, (alla prima style:1.3), oil on linen, "
                  "painterly oil on canvas, (painterly style:1.3), exquisite composition and lighting, "
                  "modern painterly masterpiece, by alexi zaitsev, award-winning painterly alla prima oil painting.",
        "negative_prompt": "detail, framed, faded colors, terrible photo, bad composition, hilariously bad drawing, "
                           "bad photo, bad anatomy, extremely high contrast, worst quality, watermarked signature, "
                           "bad colors, deformed, amputee, washed out, glare, boring colors, bad crayon drawing"
    },
    {
        "start": 73,
        "end": 78,
        "prompt": "breathtaking oil painting, Generate an oil painting of a male face fully different colored clothes "
                  "in profile view with a lot of details, focusing on skin tones and subtle shading. Include a "
                  "crowded background., photorealistic oil painting, by charlie bowater, fine details, by wlop, "
                  "trending on artstation, very detailed.",
        "negative_prompt": "low-quality, deformed, text, poorly drawn, worst quality"
    },
    {
        "start": 79,
        "end": 81,
        "prompt": "breathtaking alla prima oil painting, Create an oil painting of a bird perched on a branch, "
                  "focusing on feather texture and vibrant colors. Include a blurred background., close up, "
                  "(alla prima style:1.3), oil on linen, painterly oil on canvas, (painterly style:1.3), "
                  "exquisite composition and lighting, modern painterly masterpiece, by alexi zaitsev, award-winning "
                  "painterly alla prima oil painting.",
        "negative_prompt": "framed, faded colors, terrible photo, bad composition, hilariously bad drawing, "
                           "bad photo, bad anatomy, extremely high contrast, worst quality, watermarked signature, "
                           "bad colors, deformed, amputee, washed out, glare, boring colors, bad crayon drawing"
    },
    {
        "start": 82,
        "end": 87,
        "prompt": "breathtaking alla prima oil painting, Generate a high-resolution oil painting of a lively, "
                  "crowded library with at least fifteen people, detailed bookshelves, and warm lighting. Focus on "
                  "creating a sense of noise and movement., close up, (alla prima style:1.3), oil on linen, "
                  "painterly oil on canvas, (painterly style:1.3), exquisite composition and lighting, "
                  "modern painterly masterpiece, by alexi zaitsev, award-winning painterly alla prima oil painting.",
        "negative_prompt": "framed, faded colors, terrible photo, bad composition, hilariously bad drawing, "
                           "bad photo, bad anatomy, extremely high contrast, worst quality, watermarked signature, "
                           "bad colors, deformed, amputee, washed out, glare, boring colors, bad crayon drawing"
    },
    {
        "start": 88,
        "end": 89,
        "prompt": "A simple, cartoon-style yellow sun with a smiley face., breathtaking digital art, trending on "
                  "artstation, by atey ghailan, by greg rutkowski, by greg tocchini, by james gilleard, 8k, "
                  "high resolution, best quality",
        "negative_prompt": "low-quality, deformed, signature watermark text, poorly drawn"
    },
    {
        "start": 90,
        "end": 92,
        "prompt": "A small, cartoon-style house with a red roof and a yellow door in a green field., breathtaking "
                  "digital art, trending on artstation, by atey ghailan, by greg rutkowski, by greg tocchini, "
                  "by james gilleard, 8k, high resolution, best quality",
        "negative_prompt": "low-quality, deformed, signature watermark text, poorly drawn"
    },
    {
        "start": 93,
        "end": 94,
        "prompt": "A detailed cartoon character in a superhero costume, with some shading and defined musculature. "
                  "Action pose., breathtaking digital art, trending on artstation, by atey ghailan, "
                  "by greg rutkowski, by greg tocchini, by james gilleard, 8k, high resolution, best quality",
        "negative_prompt": "low-quality, deformed, signature watermark text, poorly drawn"
    },
    {
        "start": 95,
        "end": 100,
        "prompt": "A surrealist artwork combining dream-like imagery with unexpected juxtapositions, showcasing "
                  "depth, texture, and a complex play of light and shadow., breathtaking digital art, trending on "
                  "artstation, by atey ghailan, by greg rutkowski, by greg tocchini, by james gilleard, 8k, "
                  "high resolution, best quality",
        "negative_prompt": "low-quality, deformed, signature watermark text, poorly drawn"
    }
]


# Function to generate metadata for a single image
def generate_metadata(image_filename, image_path, prompt_text, negative_prompt_text, file_number):
    # Extract image dimensions
    with Image.open(image_path) as img:
        image_width, image_height = img.size

    # Extract file size (in bytes)
    file_size = os.path.getsize(image_path)

    # Generating fake information for [ANONYMIZED]
    student_first_name = fake.first_name()
    student_last_name = fake.last_name()
    student_id = fake.unique.random_number(digits=8)
    email_address = fake.email()
    username = fake.user_name()
    age = random.randint(18, 25)
    grade_level = random.choice(["Freshman", "Sophomore", "Junior", "Senior"])
    class_section = random.choice(["A", "B", "C"])
    school_name = fake.company()

    metadata = f"""# {file_number}

[Personal Information]
Student First Name: {student_first_name}
Student Last Name: {student_last_name}
Student ID/Number: {student_id}
Email Address: {email_address}
Username: {username}
Age: {age}
Grade/year level: {grade_level}
Class section: {class_section}
School/institution name: {school_name}

[Computer Spatiotemporal Information]
Workstation ID/Number: {fake.random_number(digits=3)}
Operating System: {random.choice(operating_systems)}
Date of Creation: {datetime.now().strftime('%Y-%m-%d')}
Time of Creation: {datetime.now().strftime('%H:%M')}
Class Name: {random.choice(class_names)}
Course Code: {random.choice(course_codes)}
Professor Name: {random.choice(professor_names)}
Semester: {random.choice(semesters)}
Academic Year: {random.choice(academic_years)}
Room Number: {random.randint(100, 300)}

[Technical/AI Model Information]
UI used: {random.choice(software_names)}
[Software Information]
Drawing Software Name: {random.choice(software_names)}

AI Model Name: {random.choice(ai_models)}
AI Model Provider: {random.choice(ai_providers)}

[Generative Educational Data]
Assignment Name: {fake.sentence(nb_words=5)}
Submission Date: {(datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')}
Submission Time: {datetime.now().strftime('%H:%M')}

[Prompt to LLM]
Prompt Text: {prompt_text}
Negative Prompt Text: {negative_prompt_text}

[AI Model Parameters]
Seed Value: {random.randint(100000000, 999999999)}
Inference Steps: {random.randint(20, 100)}
Guidance Scale: {round(random.uniform(5.0, 10.0), 1)}
Image Width: {image_width}
Image Height: {image_height}
Sampler: {random.choice(sampling_methods)}
CFG Scale: {round(random.uniform(5.0, 10.0), 1)}
Model Name: Stable Diffusion
Model Version: 2.1
VAE: vae-ft-mse-840000-ema-pruned
Clip Skip: {random.choice([1, 2])}
defaultCommentOptions width: 100%
defaultCommentOptions height: 400
guidanceScale=7

[Image File Metadata]
File Name: {image_filename}
File Format: {image_filename.split('.')[-1].upper()}
File size: {file_size} bytes
Image dimensions: {image_width}x{image_height}
"""
    return metadata


# All image files list in the folder
image_files = [f for f in os.listdir(image_dir) if f.endswith(".png")]

# Generate metadata for each image
for image_filename in image_files:
    image_path = os.path.join(image_dir, image_filename)

    # Extract file number (e.g. 1 from 1.jfif)
    file_number = int(image_filename.split('.')[0]) # Convert to integer

    # Finding the appropriate prompt and negative prompt for this file
    prompt_text = "A highly detailed and professional digital painting of a vibrant futuristic cityscape."
    negative_prompt_text = "blurry, low quality, pixelated, distorted, bad anatomy, extra limbs, text artifacts"

    for interval in prompt_intervals:
        if interval["start"] <= file_number <= interval["end"]:
            prompt_text = interval["prompt"]
            negative_prompt_text = interval["negative_prompt"]
            break

    # generate metadata
    metadata = generate_metadata(image_filename,
                                 image_path,
                                 prompt_text,
                                 negative_prompt_text,
                                 file_number)

    # Save metadata file
    metadata_filename = os.path.join(output_dir, f"{file_number}.txt")
    with open(metadata_filename, "w") as f:
        f.write(metadata)

print(f"Generated {len(image_files)} metadata files in '{output_dir}' directory.")
