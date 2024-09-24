# Fruits and Vegetables Detection API

## Overview
This project aims to classify and count various types of fruits and vegetables using a computer vision model trained on a custom dataset. The model detects and counts each type of fruit/vegetable in an image and returns the result via an API built using Flask. The solution is containerized with Docker for easy deployment.

## Features
- **Image Classification**: Detects and classifies fruits and vegetables in input images.
- **Count Estimation**: Counts the number of fruits/vegetables detected in the image.
- **Dockerized**: The solution is packaged in a Docker container for portability and scalability.
- **API**: Provides a Flask-based API for easy integration.
- **Postman Testing**: Postman can be used to test the API.

## Project Structure
Fruits_vegies_classification/
│
├── app.py                            # Main Flask application
├── Dockerfile                        # Docker configuration file
├── requirements.txt                  # Python dependencies
├── best.pt                           # Trained YOLO model weights
├── Fruit_vegetable_detection.ipynb   # Model training notebook    
├── images/                           # Sample images for testing
├── README.md                         # Project documentation


## Getting Started

### Prerequisites
Make sure you have the following tools installed on your machine:
- **Docker**: [Install Docker]
- **Postman**: [Install Postman]
- **Python 3.10+**: If running locally without Docker

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/fruits-veg-detection.git
cd fruits-veg-detection

2. Setup Using Docker
Build and run the Docker container:

docker build -t fruits-veg-detection:updated .
docker run -p 5000:5000 fruits-veg-detection:updated

3. You can pull the Docker image and run it locally.

Pull the Docker Image
docker pull atulsah/fruits-veg-detection:updated

Run the Docker Container
To start the API locally using Docker, run the following command:
docker run -p 5000:5000 atulsah/fruits-veg-detection:updated


4. Running Locally (Without Docker)

python app.py


## Model Training
The model was trained using the YOLOv8 architecture on a custom dataset of fruits and vegetables. Here's a summary of the training process:

Dataset: The dataset consists of images annotated in YOLO format.
Model: A YOLOv8 model was fine-tuned for multi-class detection.
Training Environment: Training was done on a machine with the following specs:
GPU: Nvidia RTX 3080
Framework: PyTorch
Best Model: The best model checkpoint is saved as best.pt.



## Using the API
Once the application is running, you can use the following endpoints to interact with the model.

1. Detect Fruits and Vegetables
Endpoint: /predict
Method: POST
Content-Type: multipart/form-data
Request Body:
image: The image file containing fruits/vegetables.

Example Using Postman
Open Postman.
Create a new POST request.
Set the URL to http://localhost:5000/predict.
Under the Body tab, select form-data.
Add a key image and select a file to upload.
Send the request.
Response
The API will return a JSON object containing the names and counts of detected fruits and vegetables.
{
  "detections": [
    {"fruit": "apple", "count": 3},
    {"fruit": "banana", "count": 5}
  ]
}

2. Sample Request Using curl

curl -X POST -F image=@path/to/your/image.jpg http://localhost:5000/predict

## Postman Setup
To test the API using Postman:

Open Postman and create a new POST request.
Set the request URL to http://localhost:5000/predict.
Under the Body tab, select form-data and add a key image with the image file you want to test.
Hit the "Send" button to get the prediction result.


## Acknowledgements
Ultralytics YOLOv8: For the object detection model.
Albumentations: For image augmentations.
Flask: For building the API.
Docker: For image and containerization




