# Gemini AI Multi-Tool with Streamlit

An interactive AI web application built with Streamlit and powered by Google's Gemini models.

## Features

- 🤖 **ChatBot**: Conversational AI powered by Gemini.
- 📷 **Snap Narrate (Image Captioning)**: Upload images to receive detailed descriptions and captions.
- 🔡 **Embed Text**: Generate vector embeddings for input text.
- ❓ **Ask Me Anything**: Prompt-response question answering.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <YOUR_REPOSITORY_URL>
cd pythonProj
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Configure API Key
Create a `config.json` file in the root directory (based on `config.example.json`):
```json
{
  "GOOGLE_API_KEY": "your_google_gemini_api_key_here"
}
```
*(Alternatively, you can set the `GOOGLE_API_KEY` environment variable).*

### 5. Run the Application
```bash
streamlit run main.py
```
