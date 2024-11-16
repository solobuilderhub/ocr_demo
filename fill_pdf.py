from PyPDF2 import PdfReader, PdfWriter

# Open the editable PDF
reader = PdfReader("pdf/a901_annual_update.pdf")
fields = reader.get_form_text_fields()

# Create a PdfWriter object
writer = PdfWriter()

print("total pages: ", len(reader.pages))
# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Update all fields with the value "ok"
for page in range(0, len(reader.pages)):
    for field_name in fields:
        writer.update_page_form_field_values(writer.pages[page], {field_name: "ok"})


# Save the updated PDF to a new file
with open("pdf/a901_annual_update_filled.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("All fields have been updated with the value 'ok'.")