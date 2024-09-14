import cv2
import webbrowser
from pyzbar.pyzbar import decode
from PIL import Image
import fitz  # PyMuPDF

def extract_qr_code_image_from_pdf(pdf_filename, image_filename):
    """
    Extract the first QR code image from a PDF file and save it as an image file.

    :param pdf_filename: The filename of the PDF containing the QR code.
    :param image_filename: The filename to save the extracted QR code image.
    """
    pdf_document = fitz.open(pdf_filename)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        pix.save(image_filename)
        break  # Assume the first page contains the QR code

def read_qr_code(image_filename):
    """
    Read a QR code from an image file and return the data contained in it.

    :param image_filename: The filename of the image containing the QR code.
    :return: The data decoded from the QR code.
    """
    img = cv2.cvtColor(cv2.imread(image_filename), cv2.COLOR_BGR2RGB)
    decoded_objects = decode(img)
    
    if decoded_objects:
        return decoded_objects[0].data.decode("utf-8")
    else:
        print("No QR code found in the image.")
        return None

def open_url_from_qr_code(pdf_filename):
    """
    Extract a QR code image from a PDF file, read the URL contained in the QR code,
    and open the URL in a web browser.

    :param pdf_filename: The filename of the PDF containing the QR code.
    """
    image_filename = "temp_qr_code_image.png"
    extract_qr_code_image_from_pdf(pdf_filename, image_filename)
    
    url = read_qr_code(image_filename)
    if url:
        print(f"Opening URL: {url}")
        webbrowser.open(url)
    else:
        print("Failed to decode QR code or no QR code found.")

# Example usage
pdf_filename = "example_qr_code.png"
open_url_from_qr_code(pdf_filename)
