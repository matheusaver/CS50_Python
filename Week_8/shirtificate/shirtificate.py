from fpdf import FPDF

def make_pdf(user_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 45)
    pdf.cell(0, 60, text="CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", x=0, y=70)
    pdf.set_font_size(30)
    pdf.set_text_color(255,255,255)
    pdf.text(55, 140, text=f"{user_name} took CS50")
    pdf.output("shirtificate.pdf")


user_name = input("Name: ")
output = make_pdf(user_name)
