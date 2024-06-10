#!/bin/bash

# Define the directory containing the folders
DIRECTORY="/Users/kartikmittal/Downloads/1" #Path to the directory

# List of folders to keep
KEEP_FOLDERS=(
    4650 4582 4562 4413 4366 4281 4176 4145 4128 4080 4063 4053 4004 3973 3868 3825
    3715 3687 3605 3517 3368 3366 3293 3291 3037 3024 3007 2955 2931 2922 2868 2683
    2634 2601 2594 2593 2557 2485 2430 2403 2367 2332 2309 2288 2234 2233 1987 1869
    1865 1859 1840 1839 1783 1739 1703 1646 1621 1444 1387 1337 1295 1266 1259 1252
    1213
) #Folders to keep

# Convert the array to a string of regex pattern
KEEP_PATTERN=$(printf "|%s" "${KEEP_FOLDERS[@]}")
KEEP_PATTERN=${KEEP_PATTERN:1} # Remove the leading '|'

# Iterate through all folders in the directory
for folder in "$DIRECTORY"/*; do
    # Extract the folder name
    folder_name=$(basename "$folder")
    
    # Check if the folder name is in the keep list
    if [[ ! "$folder_name" =~ ^($KEEP_PATTERN)$ ]]; then
        # If not, delete the folder
        echo "Deleting $folder"
        rm -rf "$folder"
    fi
done
