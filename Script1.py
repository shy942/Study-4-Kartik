import base64
import requests
import os

# OpenAI API Key
api_key = "YOUR_API_KEY"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your folder containing images
folder_path = "/Users/kartikmittal/LLM/ff/"
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
                        "text": "Please look at given image very carefully,look for meaningless labels, look for Cross icon, identify what is in the image and then precisely classify the elements (Yes- For Present , No - For Absent) in this image into the following categories and subcategories:\n\n"
                            "1. Programming Components\n"
                            "  a. Programming Code: If the image contains programming code of any programming language other than python.\n"
                            "  b. Exceptions/Errors:If the image contain error or exception messages.\n"
                            "  c. Stack Trace: Ordered list of API method invocations.he trace contains various structured items including class names, method names, and line numbers from the source code.\n"
                            "  d. Git Commands: Git bash commands and their output.\n"
                            "  e. Python Commands: If image contains Python code , commands and their output.\n"
                            "  f. Other Command: Other command-line instructions and their output.\n"
                            "  g. IDE for Coding: Is the image is of IDE?\n"
                            "  h. Mixed Component: Contains more than one component .Mixed UI and code elements. (More then one Yes)\n"
                            # "  i. Programming Indicator: Indicators related to programming context.\n"
                            "2. UI Components\n"
                            "  a. Non-textual UI: Graphical or visual UI elements without text labels. Examples include shapes or graphics without any accompanying text, such as a circle or icon drawn by code that does not contain a label or any textual content.\n"
                            "  b. Textual UI: UI components with meaningful text labels or content. If the image contains any text labels or descriptions, such as 'Hello, world!' or numerical values.\n"
                            "  c. Indicator: Explicitly drawn rectangles, circles or arrows that indicate specific points or areas. Note: Cross icon is not an indicator!\n"
                            "3. Natural Language Text\n"
                            "  a. English Text: Yes (if the text contains only letters (a-z, A-Z), numbers (0-9), and all symbols like commas, periods, etc.)\n"
                            "  b. Non-English Text: Yes (if the text contains characters outside the English character set)\n"
                            "  c. Mixed Language: Yes (if the text contains both English and non-English characters)\n"
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
    return result
