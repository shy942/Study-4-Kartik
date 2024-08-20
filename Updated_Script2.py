import pandas as pd
import Updated_Script1 as Script1

def parse_data(input_text):
    # Splitting the input text into lines
    lines = input_text.strip().split('\n')
    
    # Define project variables
    Project_Id = 313 #Project Number
    Project_Name = "cheat.sh" #Project Name
    
    # Extracting Image IDs
    images = [line.split(': ')[-1] for line in lines if "Processing file" in line]
    image_ids = [i[:-4] for i in images]
    
    # Initialize a dictionary to hold the data
    data = {
        "Project ID": [],
        "Project Name": [],
        "BugID": [],
        "ImageID": [],
        "Non-textual UI": [],
        "Textual UI": [],
        "Programming Code": [],
        "Exceptions/Errors": [],
        "Git Commands": [],
        "Python Commands": [],
        "Other Command": [],
        "English Text": [],
        "Non-English Text": [],
        "Mixed Language": [],
        "Indicator": []
    }
    
    # Temporary storage for the current image's data
    current_data = {key: 'No' for key in data.keys() if key not in ["ImageID", "Project ID", "Project Name", "BugID"]}
    current_data["ImageID"] = None
    current_data["Project ID"] = Project_Id
    current_data["Project Name"] = Project_Name
    current_data["BugID"] = None
    
    for line in lines:
        # Check if a new image section starts
        if "Processing file" in line:
            if current_data["ImageID"]:
                for key in current_data:
                    data[key].append(current_data[key])
            current_data = {key: 'No' for key in data.keys() if key not in ["ImageID", "Project ID", "Project Name", "BugID"]}
            image_name = line.split(': ')[-1]
            new_image_name = image_name[:-4]
            current_data["ImageID"] = new_image_name
            current_data["BugID"] = new_image_name[:-1]
            current_data["Project ID"] = Project_Id
            current_data["Project Name"] = Project_Name
        
        # Check for each category and update the current data accordingly
        if "Programming Code" in line:
            if "Yes" in line:
                current_data["Programming Code"] = "Yes"
            if "No" in line:  
                current_data["Programming Code"] = "No"
        elif "Exceptions/Errors" in line:
            if "Yes" in line:
                current_data["Exceptions/Errors"] = "Yes"
            if "No" in line:
                current_data["Exceptions/Errors"] = "No"
        elif "Git Commands" in line:
            if "Yes" in line:
                current_data["Git Commands"] = "Yes"
            if "No" in line:
                current_data["Git Commands"] = "No"
        elif "Python Commands" in line:
            if "Yes" in line:
                current_data["Python Commands"] = "Yes"
            if "No" in line:
                current_data["Python Commands"] = "No"
        elif "Other Command" in line:
            if "Yes" in line:
                current_data["Other Command"] = "Yes"
            if "No" in line:
                current_data["Other Command"] = "No"

        elif "Non-textual UI" in line:
            if "Yes" in line:
                current_data["Non-textual UI"] = "Yes"
            # if "No" in line:
            #     current_data["Non-textual UI"] = "No"
        elif "Textual UI" in line and "Non-textual UI" not in line:
            if "Yes" in line:
                current_data["Textual UI"] = "Yes"
            if "No" in line:
                current_data["Textual UI"] = "No"
        elif "Indicator" in line:
            if "Yes" in line:
                current_data["Indicator"] = "Yes"
            if "No" in line:
                current_data["Indicator"] = "No"
        elif "Non-English Text" in line:
            if "Yes" in line:
                current_data["Non-English Text"] = "Yes" 
            # if "No" in line :
            #     current_data["Non-English Text"] = "No"
        elif "English Text" in line and "Non-English Text" not in line:
            if "Yes" in line:
                current_data["English Text"] = "Yes"
            if "No" in line:
                current_data["English Text"] = "No"
        
        elif "Mixed Language" in line:
            if "Yes" in line:
                current_data["Mixed Language"] = "Yes"
            if "No" in line:
                current_data["Mixed Language"] = "No"

    # Add the last image data
    if current_data["ImageID"]:
        for key in current_data:
            data[key].append(current_data[key])

    # Creating DataFrame
    df = pd.DataFrame(data)
    
    # Saving DataFrame to CSV
    output_csv_path = 'FinalGPTClassificationProject#313.csv'
    df.to_csv(output_csv_path, index=False)
    return output_csv_path

# Sample input text
input_text = Script1.process_image("/Users/kartikmittal/LLM/313")  # Path to folder containing all images only
print(input_text)
print(type(input_text))

# Process the sample input text and save to CSV
csv_path = parse_data(input_text)
print(f'Data has been saved to {csv_path}')
