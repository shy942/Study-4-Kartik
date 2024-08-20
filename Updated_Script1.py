import base64
import requests
import os

# OpenAI API Key
api_key = "API_KEY"
# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your folder containing images
# folder_path = "/Users/kartikmittal/LLM/nre_image"
def process_image(folder_path):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Base payload template
    payload_template = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "You are a skilled programmer with expertise in various programming languages, components, and coding systems.You need to look at the given image very carefully, identify what is in the image and classify it into different categories as asked by user."},
            {
                "role": "user",
                "content": [ 
                    {
                        "type": "text",
                        "text": "Examine the given image thoroughly. First, identify whether the image is mainly composed of Programming Components, UI Components, or Overlapped Components. Next, classify the specific elements within the chosen category. Afterwards, identify and classify any Natural Language Text present in the image. Finally, check for any Indicators in the image. The classification should be done as follows:\n\n"
                        "1. Category Determination\n"
                        " a. Programming Components: If the image predominantly contains elements related to programming (such as code, errors, git commands, etc.)\n"
                        " b. UI Components: If the image predominantly contains user interface elements (such as graphical UI elements, textual UI components etc.)\n"
                        " c. Overlapped Components: If the image contains both UI components and programming components, such as textual/non-textual UI components appearing as pop-up windows alongside programming elements.\n\n"
                        "** Note: Do not classify an image as Overlapped Components if it can clearly be identified as either Programming Components or UI Components.\n\n"
                        "2. Detailed Classification\n"
                        " a. Programming Components:\n"
                        " i. Programming Code: If the image contains programming code of any programming language other than Python.\n"
                        " ii. Exceptions/Errors: If the image contains error or exception messages.\n"
                        " iii. Git Commands: Git bash commands and their output.\n"
                        " iv. Python Commands: If the image contains Python code, commands, and their output.\n"
                        " v. Other Commands: Other command-line instructions and their output.\n"
                        " b. UI Components:\n"
                        " i. Textual UI: UI components with any type of text labels or content. If the image contains any text labels or descriptions, such as 'Hello, world!' or numerical values.\n"
                        " ii. Non-textual UI: Graphical or visual UI elements without text labels dominating in the image. Examples include shapes or graphics without any accompanying text, such as a circle or icon drawn by code that does not contain a label or any textual content.\n"
                        "** Note: Do not classify an image as Non-textual UI if it can clearly be identified as Textual UI.\n\n"
                        "3. Natural Language Text\n"
                        " a. English Text: Yes (if the text contains letters (a-z, A-Z), numbers (0-9), or all symbols like commas, periods, etc.)\n"
                        " b. Non-English Text: Yes (if the text contains characters outside the English character set)\n"
                        " c. Mixed Language: Yes (if the text contains both English and non-English characters)\n"
                        "** Indicator : Yes/No, Yes if Indicator found. Graphical elements such as rectangles, circles, or arrows that are explicitly used to draw attention to specific points or areas within the UI. Indicators are typically used for annotations or to highlight important information. Note: Shapes or text within shapes that serve functional purposes, such as selection tools or content containers, should not be classified as indicators.\n\n"
                        "Based on the analysis, provide a  classification report indicating the presence or absence (Yes or No) of each subcategory within the chosen category, and always provide the classification for Natural Language Text."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": ""
                        }
                    }
                ]
            }
        ],
        "max_tokens": 500
        # "temperature":0.2
    }
    result = ""
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            base64_image = encode_image(image_path)
            
            # Update the payload with the base64 encoded image
            payload = payload_template.copy()
            payload["messages"][1]["content"][1]["image_url"]["url"] = f"data:image/jpeg;base64,{base64_image}"
            
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            response_json = response.json()
            
            # Extract the specific content you want
            desired_content = response_json['choices'][0]['message']['content']
            result +='\n'
            result +=(f"Processing file: {filename}")
            result +='\n'
            result +=(desired_content)
    print(result)
    return result
