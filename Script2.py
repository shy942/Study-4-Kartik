import pandas as pd
import Script1

def parse_data(input_text):
    # Splitting the input text into lines
    lines = input_text.strip().split('\n')

    
    # Extracting Image IDs
    images = [line.split(': ')[-1] for line in lines if "Processing file" in line]
    image_ids= []
    for i in images:
        nw = i[:-4]
        image_ids.append(nw)

    
    # Initialize a dictionary to hold the data
    data = {
        "ImageID": [],
        "Non-textual UI": [],
        "Textual UI": [],
        "Indicator": [],
        "Programming Code": [],
        "Exceptions/Errors": [],
        "Stack Trace": [],
        "Git Commands": [],
        "Python Commands": [],
        "Other Command": [],
        "IDE for Coding": [],
        "Mixed Component": [],
        "English Text": [],
        "Non-English Text": [],
        "Mixed Language": []
    }
    
    # Temporary storage for the current image's data
    current_data = {key: 'No' for key in data.keys() if key != "ImageID"}

    current_data["ImageID"] = None
    
    for line in lines:

        # Check if a new image section starts
        if "Processing file" in line:
            if current_data["ImageID"]:
                for key in current_data:
                    data[key].append(current_data[key])
            current_data = {key: 'No' for key in data.keys() if key != "ImageID"}
            image_name = line.split(': ')[-1]
            new_image_name = image_name[:-4]
            current_data["ImageID"] = new_image_name
        
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
        elif "Stack Trace" in line:

            if "Yes" in line:
                current_data["Stack Trace"] = "Yes"
            if "No" in line:
                current_data["Stack Trace"] = "No"
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
        elif "IDE for Coding" in line:

            if "Yes" in line:
                current_data["IDE for Coding"] = "Yes"
            if "No" in line:
                current_data["IDE for Coding"] = "No"
        elif "Mixed Component" in line:

            if "Yes" in line:
                current_data["Mixed Component"] = "Yes"
            if "No" in line:
                current_data["Mixed Component"] = "No"
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
    output_csv_path = 'image_classification.csv'
    df.to_csv(output_csv_path, index=False)
    return output_csv_path

# Sample input text
input_text = Script1.process_image("/Users/kartikmittal/LLM/ff/") #Path to folder containg all images only
print(input_text)
print(type(input_text))

# Process the sample input text and save to CSV
csv_path = parse_data(input_text)
print(f'Data has been saved to {csv_path}')