from flask import Flask, render_template, request, redirect, url_for, flash
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

UPLOAD_FOLDER = 'static/uploads/'
RESULT_FOLDER = 'static/results/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_hsv_values(lower, upper):
    """Validate HSV values are within valid ranges and lower <= upper"""
    valid = True
    valid &= (0 <= lower[0] <= 179) and (0 <= upper[0] <= 179)
    valid &= all(0 <= val <= 255 for val in lower[1:]) and all(0 <= val <= 255 for val in upper[1:])
    valid &= all(l <= u for l, u in zip(lower, upper))
    return valid

def hsv_filter(image_path, lower, upper):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Error reading image file")
    
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    
    return img, mask, result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # File upload handling
        if 'image' not in request.files:
            flash("No file part in the request")
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)
        
        if not allowed_file(file.filename):
            flash("Unsupported file format. Allowed formats: PNG, JPG, JPEG, BMP")
            return redirect(request.url)
        
        # Generate unique filename
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_filename = f"{timestamp}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        
        # Get and validate HSV values
        try:
            lower = np.array([
                int(request.form['lower_h']),
                int(request.form['lower_s']),
                int(request.form['lower_v'])
            ])
            upper = np.array([
                int(request.form['upper_h']),
                int(request.form['upper_s']),
                int(request.form['upper_v'])
            ])
        except (KeyError, ValueError):
            flash("Invalid HSV values. Please enter numbers only.")
            return redirect(request.url)
        
        if not validate_hsv_values(lower, upper):
            flash("Invalid HSV range. Ensure 0 ≤ Lower ≤ Upper (H: 0-179, S/V: 0-255)")
            return redirect(request.url)
        
        # Process image
        try:
            original, mask, result = hsv_filter(file_path, lower, upper)
        except Exception as e:
            flash(f"Image processing error: {str(e)}")
            return redirect(request.url)
        
        # Save results with unique names
        mask_filename = f"mask_{unique_filename}"
        result_filename = f"result_{unique_filename}"
        
        mask_path = os.path.join(app.config['RESULT_FOLDER'], mask_filename)
        result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
        
        cv2.imwrite(mask_path, mask)
        cv2.imwrite(result_path, result)
        
        return render_template('index.html', 
                               original=url_for('static', filename=f'uploads/{unique_filename}'),
                               mask=url_for('static', filename=f'results/{mask_filename}'),
                               result=url_for('static', filename=f'results/{result_filename}'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)