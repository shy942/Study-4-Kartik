This repository contains a set of scripts for managing folders, extracting images, and classifying them using OpenAI's API. The scripts are designed to automate the process of organizing and analyzing images.

# Contents


clean_folder.sh: A script to keep only selected folders and delete all others in a specified directory.
png_only.sh: A script to extract all PNG files from the remaining folders into a new folder.
script1.py: A Python script to classify images using the OpenAI API.
script2.py: A Python script to parse the output from script1.py and save the data in a CSV format.

# Scripts Overview

## clean_folder.sh
This script removes all folders in a specified directory except those listed in the KEEP_FOLDERS array.
## Usage:
Open the script and modify the DIRECTORY variable to point to your target directory.
Adjust the KEEP_FOLDERS array to include the folder names you want to keep.
Run the script using the command: bash clean_folder.sh

## png_only.sh
This script extracts all PNG files from the remaining folders into a new folder.
## Usage:
Create a new folder where you want to store the PNG files.
Modify the script to specify the source and destination directories.
Run the script using the command: bash png_only.sh

## script1.py
A Python script that uses the OpenAI API to classify images into different categories.
## Usage:
Set your OpenAI API key in the api_key variable.
Modify the folder_path variable to point to the folder containing your images.
Run the script using the command: python script1.py

## script2.py
A Python script that processes the output from script1.py and saves the classification data into a CSV file.
## Usage:
Ensure script1.py has been executed and produced an output.
Run script2.py using the command: python script2.py

# You do not need to run Script1 , Script2 is calling Script1
