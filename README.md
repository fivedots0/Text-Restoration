## Text Recovery with OpenCV and Pytesseract

This repository provides a simple implementation of text recovery from images using OpenCV and Pytesseract. The main functionality is divided into three functions:

### preprocess_image(image): This function takes an input image and performs various preprocessing steps to enhance the readability of the text. The steps include:
Converting the image to grayscale
#### Applying adaptive thresholding to binarize the image
#### Denoising the image using morphological operations
#### Dilating the image to enhance text regions
### extract_text(image, config): This function uses Pytesseract, an optical character recognition (OCR) library, to extract text from the preprocessed image. The config parameter allows you to specify additional Pytesseract configurations, such as the language model and page segmentation mode.
### text_recovery_with_ocr(image_path): This is the main function that combines the preprocessing and text extraction steps. It takes the path to the input image, preprocesses it, and then extracts the text using Pytesseract.
