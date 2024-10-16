Project Title: Pencil Sketch Image Converter
Project Description
The Pencil Sketch Image Converter is a web-based application designed to transform uploaded images into artistic pencil sketches. This project leverages the Flask framework for creating the web interface and OpenCV, a powerful computer vision library, for image processing.

Objectives
The primary objective of this project is to provide users with an easy and intuitive way to convert their photos into stunning pencil sketches. By utilizing advanced image processing techniques, the application aims to:

Allow users to upload images through a web interface.
Process the uploaded images to create a pencil sketch effect.
Provide a downloadable link for the generated sketch.
Features
User-Friendly Interface:

The application features a simple and responsive web interface, allowing users to easily upload their images.
Image Uploading:

Users can upload various image formats (e.g., JPEG, PNG) directly through the web application.
Image Processing:

The application processes the uploaded images using a combination of techniques, including:
Grayscale Conversion: Converts the image to grayscale to simplify the sketching process.
Bilateral Filtering: Reduces noise while preserving edges in the image.
Edge Detection: Employs the Canny edge detection method to highlight prominent features.
Sketch Generation: Utilizes image inversion and Gaussian blurring to create the final pencil sketch effect.
Downloadable Sketch:

After processing, users receive a link to download their converted pencil sketch, which is saved in a designated directory.
Technical Stack
Backend: Flask (Python web framework)
Image Processing: OpenCV (Python library for computer vision)
Frontend: HTML/CSS for the web interface
File Storage: Local directories for uploaded and processed images
