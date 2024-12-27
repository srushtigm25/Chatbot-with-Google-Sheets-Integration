#Library Imports

import openai
import gspread
from google.oauth2.service_account import Credentials
import tkinter as tk
from tkinter import scrolledtext

# OpenAI API key
openai.api_key = ""  # Replace with your actual API key

# Google Sheets setup
credentials_file = "service_account.json"  # Replace with the actual path
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Load credentials
credentials = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
gc = gspread.authorize(credentials)

# Access Google Sheet
sheet_id = ""  # Replace with your actual Sheet ID
sheet = gc.open_by_key(sheet_id).sheet1  # Access the first sheet

# Read data from Google Sheet
rows = sheet.get_all_values()
augmented_data = "\n".join([str(row) for row in rows])  # Convert rows to string format

# Function to query GPT
def get_gpt_response(prompt, additional_data):
    augmented_prompt = (
        f"Learn from this data {additional_data} answer the following query {prompt} based on that data. "
        "You are given a list of facts and data. Please answer the following question based on this information. "
        "Only return the relevant information or response, without any explanations or `based on the data` statements, "
        "and if you don't find it in the data I provided, give an answer based on your knowledge. "
        "Also, if the prompt has calculations, then strictly follow the data, meaning the data should only be used if it "
        "exactly matches the prompt while dealing with numerical data, and if we don't have it, give basic numerical output."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": augmented_prompt},
            ],
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

# Function to handle user input in the UI
def handle_user_input():
    user_prompt = user_input.get()
    if user_prompt.strip() == "":  # Ignore empty inputs
        return

    # Display user input in chat window
    chat_window.insert(tk.END, f"User: {user_prompt}\n")
    user_input.delete(0, tk.END)  # Clear input field

    # Get GPT response
    response = get_gpt_response(user_prompt, augmented_data)
    chat_window.insert(tk.END, f"GPT: {response}\n\n")
    chat_window.see(tk.END)  # Auto-scroll to the bottom

# Hover effects for buttons
def on_enter(e):
    e.widget['background'] = '#45a049' if e.widget['text'] == 'Send' else '#d32f2f'

def on_leave(e):
    e.widget['background'] = '#4CAF50' if e.widget['text'] == 'Send' else '#f44336'

# Initialize the UI
root = tk.Tk()
root.geometry("800x700")
root.configure(bg="#f7f7f7")
root.title("Chatbot with Google Sheets Integration")

# Fonts and styles
font_header = ("Helvetica", 16, "bold")
font_main = ("Segoe UI", 12)
button_font = ("Segoe UI", 10, "bold")

# Header
header_frame = tk.Frame(root, bg="#4CAF50", height=50)
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
header_label = tk.Label(
    header_frame, text="Machine Learning Final Project", font=font_header, bg="#4CAF50", fg="white"
)
header_label.pack(pady=10)

# Chat window
chat_window_frame = tk.Frame(root, bg="#f7f7f7")
chat_window_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=(10, 5), sticky="nsew")
chat_window = scrolledtext.ScrolledText(
    chat_window_frame, wrap=tk.WORD, state='normal', height=20, width=70,
    bg="#ffffff", fg="#333333", font=font_main, relief="flat", borderwidth=0
)
chat_window.pack(fill="both", expand=True)

# User input field
user_input_frame = tk.Frame(root, bg="#f7f7f7")
user_input_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="ew")
user_input = tk.Entry(
    user_input_frame, width=60, font=font_main, bg="#ffffff", fg="#333333",
    relief="solid", borderwidth=1
)
user_input.pack(fill="x")

# Send button
send_button = tk.Button(
    root, text="Send", command=handle_user_input, font=button_font,
    bg="#4CAF50", fg="white", relief="flat", width=10
)
send_button.grid(row=2, column=1, padx=(10, 20), pady=10, sticky="e")
send_button.bind("<Enter>", on_enter)
send_button.bind("<Leave>", on_leave)

# Quit button
quit_button = tk.Button(
    root, text="Quit", command=root.destroy, font=button_font,
    bg="#f44336", fg="white", relief="flat", width=10
)
quit_button.grid(row=3, column=1, padx=(10, 20), pady=10, sticky="e")
quit_button.bind("<Enter>", on_enter)
quit_button.bind("<Leave>", on_leave)

# Footer
footer_frame = tk.Frame(root, bg="#e0e0e0", height=30)
footer_frame.grid(row=4, column=0, columnspan=2, sticky="ew")
footer_label = tk.Label(
    footer_frame, text="Type your message and press 'Send' to chat.", font=("Segoe UI", 10), bg="#e0e0e0", fg="#555555"
)
footer_label.pack(pady=5)

# Add responsiveness
root.grid_rowconfigure(1, weight=1)  # Chat window expands if the window is resized
root.grid_rowconfigure(2, weight=0)  # Input and buttons remain fixed
root.grid_rowconfigure(4, weight=0)  # Footer stays fixed
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

# Start the UI loop
root.mainloop()

# # Stop the virtual display when the application is closed
# display.stop()

