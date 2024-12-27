# Chatbot-with-Google-Sheets-Integration
This project integrates a chatbot interface with OpenAI's GPT-4 model and Google Sheets data to provide intelligent responses based on spreadsheet content. It features a user-friendly graphical user interface (GUI) built with Tkinter.

**📚 Project Overview**

The chatbot allows users to ask questions, and responses are generated based on:
Real-time data pulled from a Google Sheet.
GPT-4's language capabilities.

**🚀 Features**

Google Sheets Integration: Fetches live data from a specified Google Sheet.
AI-Powered Responses: Utilizes OpenAI GPT-4 for generating intelligent replies.
User-Friendly GUI: Built using Tkinter with real-time chat interactions.
Error Handling: Provides meaningful error messages for API or connection failures.

**🛠️ Installation**

Prerequisites
Make sure you have the following installed:
Python 3.8+
Required libraries: openai, gspread, oauth2client, tkinter

**Setup Google Sheets API**

Enable the Google Sheets API from the Google Cloud Console.
Download your service_account.json file.
Share your Google Sheet with the service account email.
**Update the script with:**

OpenAI API Key
Google Sheets Credentials File Path
Google Sheet ID

**🖥️ Usage**

Enter your query in the input field.
Click Send to receive AI-generated responses.
Click Quit to exit the application.

**🐞 Troubleshooting**

Ensure your Google API credentials are correct.
Verify OpenAI API key validity.
Check your Google Sheet permissions.
