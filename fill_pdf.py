from PyPDF2 import PdfReader, PdfWriter

# Open the editable PDF
reader = PdfReader("pdf/a901_annual_update.pdf")
writer = PdfWriter()

# Get the fields
fields = reader.get_fields()

# Update fields with dummy text
updated_fields = {field_name: "Dummy Text" for field_name in fields}

# Iterate through each page and update the fields
for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    writer.add_page(page)
    writer.update_page_form_field_values(writer.pages[page_num], updated_fields)

# Write the updated PDF to a new file
with open("pdf/a901_annual_update_filled.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("PDF fields updated and saved to pdf/a901_annual_update_filled.pdf")