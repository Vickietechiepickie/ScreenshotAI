import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab, Image
import pytesseract
import io
import requests
import json

# Ensure the tesseract executable path is set
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Constants for the OpenAI API
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "###Replace ur open api key"

class ScreenshotTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Tool")
        self.root.geometry("300x150")

        self.label = tk.Label(root, text="Press Enter to take a screenshot.")
        self.label.pack(pady=20)

        self.root.bind("<Return>", self.take_screenshot)

    def take_screenshot(self, event):
        self.label.config(text="Taking screenshot...")
        self.root.update()

        # Take a screenshot
        image = ImageGrab.grab()

        # Extract text from the image using pytesseract
        extracted_text = self.extract_text_from_image(image)

        if extracted_text:
            # Send extracted text to OpenAI GPT for a response
            response = self.send_text_to_chatgpt(extracted_text)
            if response:
                self.show_result(response)

    def extract_text_from_image(self, image):
        try:
            # Use pytesseract to extract text from the image
            text = pytesseract.image_to_string(image)
            if text.strip():
                print("Extracted text:", text)
                return text
            else:
                messagebox.showerror("Error", "No text found in the screenshot.")
                return None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract text from the image: {str(e)}")
            return None

    def send_text_to_chatgpt(self, text):
        # Prepare the payload for the OpenAI API
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ]
        }

        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                response_json = response.json()
                return response_json['choices'][0]['message']['content']
            else:
                messagebox.showerror("Error", f"Failed to get response from API: {response.status_code} - {response.text}")
                return None
        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return None

    def show_result(self, result):
        messagebox.showinfo("API Response", result)

if __name__ == "__main__":
    root = tk.Tk()
    tool = ScreenshotTool(root)
    root.mainloop()
