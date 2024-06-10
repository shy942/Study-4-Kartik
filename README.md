This repository contains a set of scripts for managing folders, extracting images, and classifying them using OpenAI's API. The scripts are designed to automate the process of organizing and analyzing images.
#Contents
##clean_folder.sh: A script to keep only selected folders and delete all others in a specified directory.
##png_only.sh: A script to extract all PNG files from the remaining folders into a new folder.
##script1.py: A Python script to classify images using the OpenAI API.
##script2.py: A Python script to parse the output from script1.py and save the data in a CSV format.

#Scripts Overview
##clean_folder.sh
This script removes all folders in a specified directory except those listed in the KEEP_FOLDERS array.

##Usage:

Open the script and modify the DIRECTORY variable to point to your target directory.
Adjust the KEEP_FOLDERS array to include the folder names you want to keep.
Run the script using the command: bash clean_folder.sh
