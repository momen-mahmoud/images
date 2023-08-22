#images


-i just used PIL library is used to work with images and shutil for file operations and csv is used for reading and writing CSV files


-then i used extract_images function The function is responsible for processing images from the input_folder, saving them in the output_folder, and generating a CSV report in the report_csv file



-then using using the os.walk function. It iterates over directories, subdirectories, and files. For each file, it checks if the file has a valid image extension (.png, .jpg, .jpeg, .gif). If it's a valid image file, it constructs the full image_path.



-Finally, after processing each image, the image_counter is incremented to keep track of the image numbering.


To run this solution just download this repo and open the repo file in terminal and type "python images.py" thats all.
