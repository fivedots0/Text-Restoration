import cv2
import numpy as np
import pytesseract
from PIL import Image

def preprocess_image(image):
    """
    Preprocess the input image to enhance text readability.
    
    Parameters:
    image (numpy.ndarray): The input image.
    
    Returns:
    numpy.ndarray: The preprocessed image.
    """
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply adaptive thresholding to binarize the image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    # Denoise the image using morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    denoised = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    
    # Perform dilation to enhance text regions
    dilated = cv2.dilate(denoised, kernel, iterations=1)
    
    return dilated

def extract_text(image, config='-l eng --oem 1 --psm 6'):
    """
    Extract text from the preprocessed image using Pytesseract.
    
    Parameters:
    image (numpy.ndarray): The preprocessed image.
    config (str): The Pytesseract configuration string.
    
    Returns:
    str: The extracted text.
    """
    try:
        # Use Pytesseract to extract text from the image
        text = pytesseract.image_to_string(image, config=config)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

def text_recovery_with_ocr(image_path):
    """
    Perform text recovery on an image, including preprocessing and OCR.
    
    Parameters:
    image_path (str): The path to the input image.
    
    Returns:
    str: The extracted text from the image.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        
        # Preprocess the image
        preprocessed_image = preprocess_image(image)
        
        # Extract text from the preprocessed image
        extracted_text = extract_text(preprocessed_image)
        
        return extracted_text
    except Exception as e:
        print(f"Error processing image: {e}")
        return ""

# Example usage
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = text_recovery_with_ocr("tes3.png")
print(text)


