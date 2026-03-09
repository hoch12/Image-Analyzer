# Project Documentation - Image Analyzer

## Introduction & Motivation
This document outlines the complete process of building the **Image Analyzer**, an application that detects if an image contains a "middle finger" gesture. The motivation for this project is to provide a real-world tool that could be used as an automatic filter for user-uploaded content (e.g., profile pictures or forum images), filtering out inappropriate gestures before they are published.

## Requirements Fulfillment
1. **Executable Software**: It will run locally on a school PC via a modern UI (without the need for an IDE).
2. **Real-world Use Case**: Filtering potentially offensive images.
3. **Machine Learning Model**: We will create a model in a Google Colab Jupyter Notebook to classify images.
4. **Own Data Collection**: No pre-made datasets will be used. We will collect over **1500 images** containing at least **5 attributes** (MediaPipe hand landmarks) ourselves.
5. **Data Preprocessing**: We will document how the raw images were processed, scaled, and transformed into statistical attributes.
6. **Code Separation**: Any non-authorship code will be clearly isolated in the `lib` folder.
7. **Process Presentation**: This documentation serves as a timeline and explanation of the decision-making process.

## Step 1: Data Collection Strategy
Because we need absolute proof that we collected the data ourselves, and because we need at least 1500 images, we have decided to use a **Webcam Data Collection Script**.
Instead of scraping random images from the web (which could cause copyright issues and violate the "no pre-made datasets" rule), we will use OpenCV (`cv2`) to record a live feed from the webcam. The author will record themselves performing the gestures, rapidly saving frames to the disk to quickly reach the required dataset size.

*(This document will be continuously updated as the project progresses through Data Preprocessing, Model Training, and UI Development.)*
