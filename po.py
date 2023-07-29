from fpdf import FPDF

def dummy_pdf(file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.output(file_name, "F")

def generate_pdf_files():
    folder_path = "C:/Users/User/OneDrive/Desktop/PO Folders"

    for i in range(10, 101):
        file_name = f"PO-2023-{str(i).zfill(5)}.pdf"
        file_path = f"{folder_path}/{file_name}"
        dummy_pdf(file_path)
        print(f"Created File: {file_name}")

    print("Task Completete :D")

generate_pdf_files()