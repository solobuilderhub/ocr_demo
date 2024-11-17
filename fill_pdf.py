from PyPDF2 import PdfReader, PdfWriter
import json

def serialize_fields(fields):
    serialized_fields = {}
    for key, value in fields.items():
        serialized_fields[key] = {k: str(v) for k, v in value.items()}
    return serialized_fields

# Open the editable PDF
reader = PdfReader("pdf/a901_annual_update.pdf")
fields = reader.get_fields()

# Serialize fields
serialized_fields = serialize_fields(fields)

# Save the serialized fields to a JSON file
with open("a901 renewal.json", "w") as json_file:
    json.dump(serialized_fields, json_file, indent=4)

print("Fields have been saved to fields.json")

# Create a PdfWriter object
writer = PdfWriter()

print("total pages: ", len(reader.pages))

# # Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # Save the updated PDF to a new file
# with open("pdf/a901_annual_update_filled.pdf", "wb") as output_pdf:
#     writer.write(output_pdf)