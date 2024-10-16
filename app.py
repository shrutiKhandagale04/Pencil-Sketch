from flask import Flask, render_template, request
import os
from program import convert  # Ensure this is correctly importing your convert function

app = Flask(__name__)

# Configuration for the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')  # Ensure this template exists

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return "No file part"
    
    file = request.files['image']
    if file.filename == '':
        return "No selected file"

    # Save the uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Process the image using the convert function from program.py
    sketch_path = convert(file_path)
    if sketch_path is None:
        return "Error converting image to sketch"

    return f"Sketch saved at: <a href='{sketch_path}' download>Download Sketch</a>"

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the uploads folder if it doesn't exist
    app.run(debug=True)  # Run the app in debug mode
