# ScreenshotAI
Screenshot Tool with Text Extraction and OpenAI GPT Integration
This Python tool allows you to take a screenshot, extract text from the image using Tesseract OCR, and send the extracted text to OpenAI's GPT-3.5 API. The response is then displayed in a graphical interface.

Features
Capture screenshots by pressing Enter.
Extract text from screenshots using Tesseract OCR.
Send the extracted text to OpenAI's GPT-3.5 for a response.
Display the GPT response in the tool itself.
Prerequisites
1. Python
Ensure you have Python 3.x installed on your system. You can download Python from the official Python website.

2. Tesseract-OCR
Tesseract OCR is required for extracting text from screenshots. You need to install Tesseract and make sure it's correctly configured in your system's PATH.

Windows: Download and install Tesseract from this link.
Linux: Use the following command to install Tesseract:
bash
Copy code
sudo apt-get install tesseract-ocr
macOS: Install using Homebrew:
bash
Copy code
brew install tesseract
After installation, ensure that the Tesseract executable path is set correctly in your Python script. For Windows, update the following line in the script:

python
Copy code
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
3. API Key
You need an OpenAI API key to interact with GPT-3.5. Get the API key by signing up on OpenAI's website.

Setup
Clone the Repository (or create a new project and use the provided Python script).

Install Required Python Libraries: Use pip to install the required libraries:

bash
Copy code
pip install pytesseract pillow requests
Set Up OpenAI API Key: Replace the placeholder API_KEY in the script with your actual OpenAI API key:

python
Copy code
API_KEY = "your_openai_api_key_here"
Verify Tesseract Installation: Make sure that the Tesseract path is correctly configured. For Windows, update this line:

python
Copy code
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Running the Tool
Once the setup is complete:

Open a terminal or command prompt and navigate to the project directory.

Run the script:

bash
Copy code
python your_script_name.py
The GUI will open. Press Enter to take a screenshot. The tool will:

Capture the screenshot.
Extract any text present in the screenshot using Tesseract.
Send the extracted text to OpenAI's GPT-3.5 API.
Display the response from GPT in a message box.
Code Explanation
Libraries Used
Tkinter: Provides the graphical user interface for the tool.
Pillow (PIL): Used for taking screenshots and image processing.
Pytesseract: Used for Optical Character Recognition (OCR) to extract text from images.
Requests: Used to make API requests to OpenAI's GPT-3.5.
Core Functions
take_screenshot: Captures the screenshot when the user presses Enter.
extract_text_from_image: Uses pytesseract to extract text from the screenshot.
send_text_to_chatgpt: Sends the extracted text to OpenAI's GPT-3.5 API and retrieves the response.
show_result: Displays the GPT-3.5 response in a message box.
Error Handling
The tool provides error messages in case:

No text is found in the screenshot.
The OpenAI API request fails.
Example
Screenshot Tool Interface:

Open the tool.
Press Enter to capture the screen.
If text is detected in the image, it will be extracted and sent to OpenAI GPT.
A message box will display the GPT response.
Troubleshooting
Tesseract not found:

Ensure that the Tesseract executable path is correctly set in the script.
Verify the installation by running tesseract in your command prompt or terminal.
API Response Errors:

Double-check the API key and ensure it's valid.
Make sure that the internet connection is working.
No text extracted from screenshots:

Try taking a clearer screenshot with readable text. Pytesseract works best with high-quality images.
Future Improvements
Add the ability to configure Tesseract language settings for non-English text.
Include options to select specific areas of the screen for screenshots.
Add more customization for the GPT-3 request parameters.
License
This project is open-source and available under the MIT License.

Acknowledgments
Tesseract OCR for text extraction.
OpenAI for the GPT-3 API.
