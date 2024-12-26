import pdfplumber
import pandas as pd

# Path to the PDF file
pdf_path = "statement/rbc/rbc_cheque.pdf"

# Initialize an empty list to store transaction details
transactions = []

# Function to process text and extract relevant details
def process_page_text(text):
    lines = text.split("\n")
    print(lines)
    print("----------------------------------------------------")

# Open the PDF and process each page
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            process_page_text(text)


print(transactions)
# Clean up and parse transactions into a DataFrame
# if transactions:
#     # Example parsing logic: Assuming columns like 'Date', 'Description', 'Debit', 'Credit', 'Balance'
#     data = []
#     for txn in transactions:
#         parts = txn.split()
#         date = parts[0]
#         description = " ".join(parts[1:-3])  # Extract description
#         debit = parts[-3] if "-" in parts[-3] else "0.00"  # Debits are often negative
#         credit = parts[-2] if "-" not in parts[-2] else "0.00"  # Credits are positive
#         balance = parts[-1]  # Final balance
        
#         data.append([date, description, debit, credit, balance])
    
#     # Create a DataFrame for easy readability
#     df = pd.DataFrame(data, columns=["Date", "Description", "Debit", "Credit", "Balance"])
#     print(df)
# else:
#     print("No transactions found.")

