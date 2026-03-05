# Photo-enhancer

Image Enhancement Web App

This project is a Flask-based web application that enhances image quality using computer vision techniques.
Users can upload an image, and the system automatically denoises, sharpens, and improves the image, while also generating a comparison of brightness, contrast, and sharpness.

Project Structure

app.py – Main Flask application that handles image upload and rendering.

enhancer.py – Image processing logic using OpenCV.

requirements.txt – Python dependencies required to run the project.

static/ – Stores uploaded images, enhanced images, and generated charts.

templates/ – HTML frontend for the web interface.

Features

Upload image through web interface

Automatic image denoising

Image sharpening and enhancement

Calculate image statistics:

Brightness

Contrast

Sharpness

Generate comparison chart

Display original vs enhanced image

Technologies Used

Python

Flask

OpenCV

NumPy

Matplotlib
