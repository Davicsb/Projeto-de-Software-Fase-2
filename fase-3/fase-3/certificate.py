from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from datetime import datetime
from reportlab.lib import colors
import PyPDF2
import os

def fill_and_generate_certificate(student):
    if student is None:
        print("Student not found!")
        return None
    name = student.username
    course_name = student.course
    student_id = student.id
    date = datetime.now().strftime("%B %d, %Y")
    
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    
    c.setFillColor(colors.black)
    c.rect(30, 550, 550, 250, fill=1)
    c.setFillColor(colors.black)
    c.rect(30, 550, 550, 250, fill=0)
    
    c.setFont("Helvetica-Bold", 20)
    c.drawString(180, 800, "Certificate of Completion")
    
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 740, f"Student: {name}")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 710, f"Course: {course_name}")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 680, f"Student ID: {student_id}")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 650, f"Date: {date}")
    
    c.line(100, 600, 500, 600)
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(100, 590, "Instructor's Signature")
    
    c.save()
    packet.seek(0)
    
    output_pdf = PyPDF2.PdfWriter()
    new_pdf = PyPDF2.PdfReader(packet)
    page = new_pdf.pages[0]
    output_pdf.add_page(page)
    
    output_filename = f"{name}_certificate_filled.pdf"
    
    with open(output_filename, "wb") as output_file:
        output_pdf.write(output_file)
    
    print(f"Certificate generated successfully: {output_filename}")
    return output_filename