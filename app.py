from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
RESULT_FOLDER = 'static/results/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

def hsv_filter(image_path, lower, upper):
    img = cv2.imread(image_path)
    converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(converted, lower, upper)
    res = cv2.bitwise_and(img, img, mask=mask)
    return img, mask, res

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # استلام الصورة والقيم 
        file = request.files['image']
        lower = np.array([int(request.form['lower_h']), int(request.form['lower_s']), int(request.form['lower_v'])])
        upper = np.array([int(request.form['upper_h']), int(request.form['upper_s']), int(request.form['upper_v'])])
        
        if file:
            # حفظ الصورة في  uploads
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # تطبيق HSV Filter
            img, mask, res = hsv_filter(file_path, lower, upper)

            # حفظ النتائج في  results
            mask_path = os.path.join(app.config['RESULT_FOLDER'], f'mask_{file.filename}')
            res_path = os.path.join(app.config['RESULT_FOLDER'], f'result_{file.filename}')
            cv2.imwrite(mask_path, mask)
            cv2.imwrite(res_path, res)

            return render_template('index.html', original=url_for('static', filename=f'uploads/{file.filename}'),
                                   mask=url_for('static', filename=f'results/mask_{file.filename}'),
                                   result=url_for('static', filename=f'results/result_{file.filename}'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
