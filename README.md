# **Code Overview**
**app.py:** Main entry point for the Flask application. Contains the /api/detect route for handling file uploads and invoking the PII detection logic.


**file_reader.py:** Functions for reading text and extracting images from various file formats (e.g., PDF, Excel, HTML).


**pii_detective.py:** Functions for detecting PII using regex patterns and Keras model. It integrates both text-based and image-based detection.


**pii_regex.py:** Contains regex patterns for detecting various types of PII such as phone numbers, email addresses, and more.


**processing.py:** Functions for preprocessing images for Keras model input.


**aadhar_card_model.keras:** Keras model file used for detecting PII from images. Ensure this file is in the same directory as app.py or adjust the path in the code.


# Dependencies
Flask: Web framework for building the API.
Flask-Cors: Middleware for handling Cross-Origin Resource Sharing (CORS).
Requests: HTTP library for fetching images from URLs.
BeautifulSoup4: Library for parsing HTML.
python-docx: Library for reading DOCX files.
PyPDF2: Library for reading PDF files.
pdfminer.six: Library for extracting text from PDF files.
Pytesseract: OCR library (optional, based on code usage).
Pillow: Imaging library for handling images.
TensorFlow: Library for machine learning and running Keras models.
OpenPyXL: Library for reading Excel files.
FitZ: PyMuPDF library for extracting images from PDFs.
