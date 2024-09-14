import qrcode
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4, 
    )
    
    qr.add_data(data)
    qr.make(fit=True)  

    img = qr.make_image(fill='black', back_color='white')

    img.save(filename)
    print(f"QR code saved as {filename}")



def create_pdf_with_qr(image_filename, pdf_filename):
  
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawImage(image_filename, 100, 500, 200, 200)
    c.save()
    print(f"PDF saved as {pdf_filename}")

# Usual Image
data = "https://t.me/shahriorovv_a"
image_filename = "example_qr_code.png"
generate_qr_code(data, image_filename)

# PDF
pdf_filename = "example_qr_code2.pdf"
create_pdf_with_qr(image_filename, pdf_filename)