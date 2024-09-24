import torch
from ultralytics import YOLO
from flask import Flask, request, jsonify
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)

# Load your pre-trained model (best.pt file)
model = YOLO('best.pt')  
# Function to handle image classification and counting
def classify_and_count(image):
    results = model(image)  
    classes_count = {}

    # Iterate over the detections and count classes
    for result in results:
        for box in result.boxes:
            class_name = model.names[int(box.cls[0])]  
            if class_name in classes_count:
                classes_count[class_name] += 1
            else:
                classes_count[class_name] = 1

    return classes_count

# API Endpoint for image classification
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Read the image file
    img_bytes = file.read()
    image = Image.open(io.BytesIO(img_bytes))

    # Run the model and get classification results
    result = classify_and_count(image)

    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
