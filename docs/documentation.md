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

## Architectural Standards & Configuration
To maintain a clean and modular codebase, absolutely all static parameters (file paths, search queries, machine learning labels, iteration counts) have been extracted entirely into **`src/config.py`**. 
- No python script contains "magic numbers" or hardcoded paths.
- Code logic is fully separated from configuration state.
- Documentation and the `changelog.md` are strictly synchronized with every system change.

## Step 1: Data Collection Strategy
Because we need absolute proof that we collected the data ourselves, and because we need at least 1500 images, we initially planned to use a webcam script. However, to preserve user privacy and increase dataset variety, we pivoted to **Web Crawling/Scraping**.
We used the `icrawler` (BingImageCrawler) library to automatically search and download images from the internet based on 30+ diverse queries (e.g., "person wearing glasses middle finger", "group selfie", "empty room"). This safely and provably generated a dataset of **over 2500 unique images**, split between the "middle_finger" and "other" classes.

## Step 2: Data Preprocessing & Feature Extraction
To fulfill the requirement of parsing the data into at least 5 attributes, we are using Google's **MediaPipe Hands** framework.
The bulk extraction of the 2500+ collected images is handled exclusively by the Google Colab Notebook (`notebooks/Model_Training.ipynb`) to bypass local macOS compatibility issues. 

For the core architecture, the mathematical extraction logic (converting an image into exactly **63 numerical attributes** - 3D coordinates for 21 hand landmarks) is modularized in **`src/features.py`**. If no hand is found (e.g., in our "empty room" background pictures), the extraction returns `None`, ensuring our ML dataset remains purely numeric and mathematically precise. The output of the Colab training phase is a robust CSV tabular format ready for ML training.

## Step 3: Model Performance
Based on the latest training session, the model achieves the following metrics on unseen data (20% test split):
- **Overall Accuracy: 80.97%**
- **Precision (Middle Finger): 82%**
- **Recall (Middle Finger): 69%**
- **F1-Score (Middle Finger): 75%**

Tato přesnost je pro demonstraci v rámci školního projektu plně dostačující. Vyšší přesnosti by bylo možné dosáhnout zvětšením datasetu o fotografie rukou z různých úhlů.

## Step 4: GUI Application & User Experience
The final delivery is a desktop application built with `CustomTkinter`. 
- **Simplicity**: Users can analyze images via a standard file dialog.
- **Visual Feedback**: Real-time status update (Safe vs Vulgar) with a color-coded confidence bar.
- **Transparency**: A sidebar provides technical details (model type, accuracy, recall) and links to the source code.
- **Customization**: Support for Light, Dark, and System appearance modes.
