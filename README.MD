# HSV Filter App

## Description
The HSV Filter App is a web application that allows users to upload images and apply HSV filtering to modify the color range. Users can adjust the Hue, Saturation, and Value (HSV) settings dynamically and download the resulting filtered images. The app is built with Python using the Flask framework for the backend and includes a simple frontend interface for user interaction.

## Features
- Upload images for processing.
- Adjust HSV ranges using sliders.
- Preview filtered images in real time.

## Installation

### Prerequisites
Ensure you have Python installed (version 3.7 or higher). Install the required dependencies listed in `requirements.txt`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/HSV_Filter_App.git
   cd HSV_Filter_App
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure
```
HSV_Filter_App/
│
├── app.py
├── requirements.txt
├── static/
│   ├── styles.css
│   ├── uploads/
│   └── results/
├── templates/
│   └── index.html
└── README.md
```

## How to Use
1. Upload an image through the interface.
2. Adjust the sliders to set the desired HSV range.
3. Click "Analyze" to preview the filtered image.



---
