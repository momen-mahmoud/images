import os
import shutil
from PIL import Image
import csv
from datetime import datetime

def extract_images(input_folder, output_folder, report_csv):
    # Create necessary folders
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize the CSV report
    with open(report_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Image Name', 'Image Size', 'Last Modification Date'])

    prefix_to_discard = "prefix_to_discard"  # Replace with your actual prefix
    image_counter = 1  # Counter for renaming images

    # Traverse the dataset directory
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_path = os.path.join(root, file)

                # Extract image name without prefix
                image_name = file[len(prefix_to_discard):]  # Remove the prefix
                new_image_name = f"image{image_counter}.jpg"  # New image name with counter

                # Copy image to output folder with new name
                new_image_path = os.path.join(output_folder, new_image_name)
                shutil.copy(image_path, new_image_path)

                # Get image size and modification date
                image = Image.open(image_path)
                image_size = os.path.getsize(new_image_path)
                modification_date = os.path.getmtime(image_path)

                # Convert modification date to MM/DD/YYYY format
                formatted_date = datetime.fromtimestamp(modification_date).strftime('%m/%d/%Y')

                # Append information to the CSV report
                with open(report_csv, 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow([new_image_name, image_size, formatted_date])

                image_counter += 1  # Increment the counter for the next image

if __name__ == "__main__":
    input_dataset_folder = "C:\\Users\\momen\\Desktop\\dairies"
    output_images_folder = "C:\\Users\\momen\\Desktop\\images_dataset"
    report_csv_file = "C:\\Users\\momen\\Desktop\\report.csv"

    extract_images(input_dataset_folder, output_images_folder, report_csv_file)
