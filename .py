# import pdfkit

# def save_webpage_as_pdf(url, output_path='E:\\Documents\\main_project\\output.pdf'):
#     try:
#         # Configure the path to wkhtmltopdf executable
#         config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

#         # Convert the webpage to PDF
#         pdfkit.from_url(url, output_path, configuration=config)

#         print(f"PDF saved successfully at: {output_path}")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage
# url_to_convert = 'https://abishek.in'
# output_pdf_path = 'E:\\Documents\\main_project\\output.pdf'
# save_webpage_as_pdf(url_to_convert, output_pdf_path)


# age=22
# drink="milk" if age<21 else "beer"
# print(f"{drink} is good for a {age}-year-old.")