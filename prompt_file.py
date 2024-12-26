prompt = """
**Task Overview**:  
I am building a web app for accounting and tax purposes with GnuCash as the backend. From a provided PDF containing transaction details, I need to extract all transactions and map them to the appropriate accounts to create a double-entry journal. Each transaction should include the mapped accounts and amounts. If a transaction cannot be mapped to any account, it should be assigned to `"None"`.  

**Response Format**:  
Return the output strictly as JSON. Do not include any additional text, commentary, or exclude any content from the PDF. Use the following schema:  

```json
"transactions": [
  {
    "description": "Transaction Description Here",
    "date": "Transaction Date Here",
    "entries": [
      {
        "account_name": "Mapped Account Name Here",
        "amount": Transaction Amount Here
      },
      {
        "account_name": "Mapped Account Name Here",
        "amount": Transaction Amount Here
      }
    ]
  }
]
```

**Account Mapping Guidelines**:  
Below are the account full names and their types. Map each transaction to the most appropriate account based on its description and context:  

1. **Assets** (Type: ASSET)  
   - Assets:Current Assets  
     - Assets:Current Assets:Checking Account (Type: BANK)  
     - Assets:Current Assets:Savings Account (Type: BANK)  
     - Assets:Current Assets:Cash in Wallet (Type: CASH)  

2. **Liabilities** (Type: LIABILITY)  
   - Liabilities:Credit Card (Type: CREDIT)  

3. **Income** (Type: INCOME)  
   - Income:Bonus  
   - Income:Gifts Received  
   - Income:Interest Income  
     - Income:Interest Income:Checking Interest  
     - Income:Interest Income:Other Interest  
     - Income:Interest Income:Savings Interest  
   - Income:Other Income  
   - Income:Salary  

4. **Expenses** (Type: EXPENSE)  
   - Expenses:Adjustment  
   - Expenses:Auto  
     - Expenses:Auto:Fees  
     - Expenses:Auto:Fuel  
     - Expenses:Auto:Parking  
     - Expenses:Auto:Repair and Maintenance  
   - Expenses:Bank Service Charge  
   - Expenses:Books  
   - Expenses:Cable  
   - Expenses:Charity  
   - Expenses:Clothes  
   - Expenses:Computer  
   - Expenses:Dining  
   - Expenses:Education  
   - Expenses:Entertainment  
     - Expenses:Entertainment:Music/Movies  
     - Expenses:Entertainment:Recreation  
     - Expenses:Entertainment:Travel  
   - Expenses:Gifts  
   - Expenses:Groceries  
   - Expenses:Hobbies  
   - Expenses:Insurance  
     - Expenses:Insurance:Auto Insurance  
     - Expenses:Insurance:Health Insurance  
     - Expenses:Insurance:Life Insurance  
   - Expenses:Laundry/Dry Cleaning  
   - Expenses:Medical Expenses  
   - Expenses:Miscellaneous  
   - Expenses:Online Services  
   - Expenses:Phone  
   - Expenses:Public Transportation  
   - Expenses:Subscriptions  
   - Expenses:Supplies  
   - Expenses:Taxes  
     - Expenses:Taxes:Federal  
     - Expenses:Taxes:Medicare  
     - Expenses:Taxes:Other Tax  
     - Expenses:Taxes:Social Security  
     - Expenses:Taxes:State/Province  
   - Expenses:Utilities  
     - Expenses:Utilities:Electric  
     - Expenses:Utilities:Garbage collection  
     - Expenses:Utilities:Gas  
     - Expenses:Utilities:Water  

5. **Equity** (Type: EQUITY)  
   - Equity:Opening Balances  

**Important Notes**:  
- **Unmapped Transactions**: If no suitable account is found, assign `"account_name": "None"`.  
- **Double-Entry**: Ensure every transaction has balanced debit and credit entries.  
- **No Text**: Output JSON directly without explanatory text or omitted content from the PDF.


"""



prompt_cheque_account = """
**Task Overview**:
I am building a web app for accounting and tax purposes with GnuCash as the backend. From a provided PDF containing transaction details, I need to extract all transactions and map them to the appropriate accounts to create a double-entry journal. 
Each transaction should include the mapped accounts and amounts. 
If a transaction cannot be mapped to any account, it should be assigned to `"None"`. 

Remember that this statement is a checking account statement, so the transactions are related to a checking account for the business.
There are 2 columns in the statement, one for the debit and one for the credit. Since this is a checking account, the debit column represents the expenses and the credit column represents the income.


**Response Format**:
Return the output strictly as JSON. Do not include any additional text, commentary, or exclude any content from the PDF. Use the following schema:

```json
"transactions": [
  {
    "date": "Transaction Date Here",
    "description": "Transaction Description Here",
    "entries": [
      {
        "account_name": "Mapped Account Name Here",
        "amount": Transaction Amount Here
      },
      {
        "account_name": "Mapped Account Name Here",
        "amount": Transaction Amount Here
      }
    ]
  }
]
```

**Account Mapping Guidelines**:
Below are the account full names and their types. Map each transaction to the most appropriate account based on its description and context:

1. **Assets** (Type: ASSET)
   - Assets:Current Assets
     - Assets:Current Assets:Checking Account (Type: BANK)
     - Assets:Current Assets:Savings Account (Type: BANK)
     - Assets:Current Assets:Cash in Wallet (Type: CASH)

2. **Liabilities** (Type: LIABILITY)
    - Liabilities:Credit Card (Type: CREDIT)

3. **Income** (Type: INCOME)
    - Income:Bonus
    - Income:Gifts Received
    - Income:Interest Income
        - Income:Interest Income:Checking Interest
        - Income:Interest Income:Other Interest
        - Income:Interest Income:Savings Interest
    - Income:Other Income
    - Income:Salary

4. **Expenses** (Type: EXPENSE)  
   - Expenses:Adjustment  
   - Expenses:Auto  
     - Expenses:Auto:Fees  
     - Expenses:Auto:Fuel  
     - Expenses:Auto:Parking  
     - Expenses:Auto:Repair and Maintenance  
   - Expenses:Bank Service Charge  
   - Expenses:Books  
   - Expenses:Cable  
   - Expenses:Charity  
   - Expenses:Clothes  
   - Expenses:Computer  
   - Expenses:Dining  
   - Expenses:Education  
   - Expenses:Entertainment  
     - Expenses:Entertainment:Music/Movies  
     - Expenses:Entertainment:Recreation  
     - Expenses:Entertainment:Travel  
   - Expenses:Gifts  
   - Expenses:Groceries  
   - Expenses:Hobbies  
   - Expenses:Insurance  
     - Expenses:Insurance:Auto Insurance  
     - Expenses:Insurance:Health Insurance  
     - Expenses:Insurance:Life Insurance  
   - Expenses:Laundry/Dry Cleaning  
   - Expenses:Medical Expenses  
   - Expenses:Miscellaneous  
   - Expenses:Online Services  
   - Expenses:Phone  
   - Expenses:Public Transportation  
   - Expenses:Subscriptions  
   - Expenses:Supplies  
   - Expenses:Taxes  
     - Expenses:Taxes:Federal  
     - Expenses:Taxes:Medicare  
     - Expenses:Taxes:Other Tax  
     - Expenses:Taxes:Social Security  
     - Expenses:Taxes:State/Province  
   - Expenses:Utilities  
     - Expenses:Utilities:Electric  
     - Expenses:Utilities:Garbage collection  
     - Expenses:Utilities:Gas  
     - Expenses:Utilities:Water  

5. **Equity** (Type: EQUITY)  
   - Equity:Opening Balances  

**Important Notes**:  
- **Unmapped Transactions**: If no suitable account is found, assign `"account_name": "None"`.  
- **Double-Entry**: Ensure every transaction has balanced debit and credit entries.  
- **No Text**: Output JSON directly without explanatory text or omitted content from the PDF.


"""


prompt_for_text = """ 
**Task Overview**:  
I am building a web app for accounting and tax purposes with GnuCash as the backend. From a provided texts containing transaction details, I need to extract all transactions and map them to the appropriate accounts to create a double-entry journal. Each transaction should include the mapped accounts and amounts. If a transaction cannot be mapped to any account, it should be assigned to `"None"`.  

**Response Format**:  
Return the output strictly as JSON. Do not include any additional text, commentary, or exclude any content from the PDF. Use the following schema:  

```json
"transactions": [
  {
    "date": "transaction date"
    "description": "Transaction Description Here",
    "entries": [
      {
        "account_name": "Mapped Account Name Here",
        "amount": Transaction Amount Here
      },
      {
        "account_name": "Mapped Account Name Here",
        "amount": Transaction Amount Here
      }
    ]
  }
]
```

**Account Mapping Guidelines**:  
Below are the account full names and their types. Map each transaction to the most appropriate account based on its description and context:  

1. **Assets** (Type: ASSET)  
   - Assets:Current Assets  
     - Assets:Current Assets:Checking Account (Type: BANK)  
     - Assets:Current Assets:Savings Account (Type: BANK)  
     - Assets:Current Assets:Cash in Wallet (Type: CASH)  

2. **Liabilities** (Type: LIABILITY)  
   - Liabilities:Credit Card (Type: CREDIT)  

3. **Income** (Type: INCOME)  
   - Income:Bonus  
   - Income:Gifts Received  
   - Income:Interest Income  
     - Income:Interest Income:Checking Interest  
     - Income:Interest Income:Other Interest  
     - Income:Interest Income:Savings Interest  
   - Income:Other Income  
   - Income:Salary  

4. **Expenses** (Type: EXPENSE)  
   - Expenses:Adjustment  
   - Expenses:Auto  
     - Expenses:Auto:Fees  
     - Expenses:Auto:Fuel  
     - Expenses:Auto:Parking  
     - Expenses:Auto:Repair and Maintenance  
   - Expenses:Bank Service Charge  
   - Expenses:Books  
   - Expenses:Cable  
   - Expenses:Charity  
   - Expenses:Clothes  
   - Expenses:Computer  
   - Expenses:Dining  
   - Expenses:Education  
   - Expenses:Entertainment  
     - Expenses:Entertainment:Music/Movies  
     - Expenses:Entertainment:Recreation  
     - Expenses:Entertainment:Travel  
   - Expenses:Gifts  
   - Expenses:Groceries  
   - Expenses:Hobbies  
   - Expenses:Insurance  
     - Expenses:Insurance:Auto Insurance  
     - Expenses:Insurance:Health Insurance  
     - Expenses:Insurance:Life Insurance  
   - Expenses:Laundry/Dry Cleaning  
   - Expenses:Medical Expenses  
   - Expenses:Miscellaneous  
   - Expenses:Online Services  
   - Expenses:Phone  
   - Expenses:Public Transportation  
   - Expenses:Subscriptions  
   - Expenses:Supplies  
   - Expenses:Taxes  
     - Expenses:Taxes:Federal  
     - Expenses:Taxes:Medicare  
     - Expenses:Taxes:Other Tax  
     - Expenses:Taxes:Social Security  
     - Expenses:Taxes:State/Province  
   - Expenses:Utilities  
     - Expenses:Utilities:Electric  
     - Expenses:Utilities:Garbage collection  
     - Expenses:Utilities:Gas  
     - Expenses:Utilities:Water  

5. **Equity** (Type: EQUITY)  
   - Equity:Opening Balances  

**Important Notes**:  
- **Unmapped Transactions**: If no suitable account is found, assign `"account_name": "None"`.  
- **Double-Entry**: Ensure every transaction has balanced debit and credit entries.  
- **No Text**: Output JSON directly without explanatory text or omitted content from the PDF.


"""

text = """
Below is the texts extracted from the PDF file of a checking account statement for a business. The transactions are related to a checking account for the business. The debit column represents the expenses and the credit column represents the income.
Please extract all transactions and map them to the appropriate accounts to create a double-entry journal. Each transaction should include the mapped accounts and amounts. If a transaction cannot be mapped to any account, it should be assigned to "None".
Please follow the account mapping guidelines provided in the system prompt and respond with the output in the specified JSON format mentioned in the system prompt.

Since this is a checking account statement, the transactions are related to a checking account for the business. The debit column represents the expenses and the credit column represents the income.
Since I want to enter the transactions into GNUcash, please ensure the debit and credit entries are balanced for each transaction with appropriate sign conventions.
For example, a debit entry should be represented as a positive amount and a credit entry as a negative amount.

Below is the extracted text from the PDF file: \n\n
RBBDA30000_1818714E D 02169 00218
1683778ALBERTALTD.
SUITE232
144052STNE
CALGARYAB T2A4T8ROYALBANKOFCANADA
P.O.BAGSERVICE2650
CALGARYAB T2P2M7
1of5BusinessAccountStatement
December7,2022toJanuary6,2023
AccountSummaryforthisPeriod
RBCDigitalChoiceBusinessTMaccountpackage
RoyalBankofCanada
264052NDSTNE-UNIT100,CALGARY,AB T1Y3R6
OpeningbalanceonDecember7,2022 $41,453.43
Totaldeposits&credits(75) +12,253.56
Totalcheques&debits(13) -11,097.26
ClosingbalanceonJanuary6,2023 = $42,609.73Accountnumber: 02169 103-766-2        
Howtoreachus:
PleasecontactyourRBCBankingrepresentativeorcall
1-800-Royal®2-0
(1-800-769-2520)
www.rbcroyalbank.com/business
AccountActivityDetails
Date Description Cheques&Debits($) Deposits&Credits($) Balance($)
Openingbalance 41,453.43
08Dec MiscPayment SKIPTHEDISHES 399.95
VSADEP05782370 19.64
MCDEP05782370 30.00
EF120805782370 335.85 42,238.87
09Dec MiscPayment 144052Street 16.76
MCDEP05782370 54.05
EF120905782370 494.77 42,804.45
12Dec MCDEP05782370 9.98
VSADEP05782370 18.49
MCDEP05782370 24.80
VSADEP05782370 68.07
EF121205782370 137.91BusinessAccountStatement
2of5December7,2022toJanuary6,2023
Accountnumber: 02169 103-766-2
AccountActivityDetails-continued
Date Description Cheques&Debits($) Deposits&Credits($) Balance($)
12Dec12Dec EF121005782370 251.69 43,315.39
13Dec MCDEP05782370 14.08
VSADEP05782370 41.68
EF121305782370 371.89 43,743.04
14Dec VSADEP05782370 18.38
MCDEP05782370 66.46
EF121405782370 325.65
Cheque-1322 539.26
Cheque-1321 600.00 43,014.27
15Dec MiscPayment SKIPTHEDISHES 301.78
VSADEP05782370 25.99
MCDEP05782370 92.21
EF121505782370 388.98 43,823.23
16Dec MiscPayment 144052Street 65.44
VSADEP05782370 10.40
MCDEP05782370 46.89
EF121605782370 374.48 44,320.44
19Dec VSADEP05782370 11.81
MCDEP05782370 53.76
EF121705782370 328.56 44,714.57
20Dec MiscPayment UberHoldingsC 8.27
MCDEP05782370 76.05
VSADEP05782370 117.52
EF122005782370 547.28
OnlineBankingtransfer-5030 3,685.86 41,777.83
21Dec MCDEP05782370 17.77
VSADEP05782370 56.15
EF122105782370 292.19 42,143.94
22Dec MiscPayment SKIPTHEDISHES 628.72
MCDEP05782370 28.90
EF122205782370 322.59 43,124.15
23Dec MiscPayment 144052Street 14.53
VSADEP05782370 56.37
EF122305782370 447.20 43,642.25
28Dec EF122605782370 50.89
VSADEP05782370 61.65
VSADEP05782370 69.71ROYALBANKOFCANADA
P.O.BAGSERVICE2650
CALGARYAB T2P2M7BusinessAccountStatement
3of5December7,2022toJanuary6,2023
Accountnumber: 02169 103-766-2
AccountActivityDetails-continued
Date Description Cheques&Debits($) Deposits&Credits($) Balance($)
28Dec28Dec EF122405782370 164.33
EF122705782370 196.73 44,185.56
29Dec MiscPayment SKIPTHEDISHES 356.54
VSADEP05782370 48.48
MCDEP05782370 103.51
EF122905782370 508.43 45,202.52
30Dec MiscPayment 144052Street 10.67
VSADEP05782370 13.59
MCDEP05782370 126.28
EF123005782370 233.78 45,586.84
03Jan MONREV05782370 0.16
VSADEP05782370 23.00
VSADEP05782370 49.74
VSADEP05782370 76.56
MCDEP05782370 87.03
MCDEP05782370 132.83
EF010305782370 177.09
EF010205782370 394.60
EF123105782370 422.61
PayEmployee-Vendor OFI002@00.85 1.70
MCFEE05782370 17.54
VSAFEE05782370 18.09
INTFEE05782370 25.50
MONFEE05782370 39.90
MiscPayment PAY-FILEFEES 2.00
CommercialRent FCAMLP 2,823.18 44,022.55
Monthlyfee 5.00
Regulartransactionfee 2 Drs@ 2.50 5.00 44,012.55
04Jan VSADEP05782370 23.57
MCDEP05782370 45.16
EF010405782370 364.50 44,445.78
05Jan MiscPayment SKIPTHEDISHES 189.51
MCDEP05782370 70.49
EF010505782370 349.81 45,055.59
06Jan MiscPayment 144052Street 28.23
MCDEP05782370 55.40BusinessAccountStatement
4of5December7,2022toJanuary6,2023
Accountnumber: 02169 103-766-2
AccountActivityDetails-continued
Date Description Cheques&Debits($) Deposits&Credits($) Balance($)
06Jan06Jan VSADEP05782370 190.59
EF010605782370 614.15
DirectDeposits(PDS)servicetotal
PAYEMP-VENDOR 3,334.23 42,609.73
Closingbalance 42,609.73
AccountFees: $11.70ROYALBANKOFCANADA
P.O.BAGSERVICE2650
CALGARYAB T2P2M7
5of5BusinessAccountStatement
December7,2022toJanuary6,2023
Accountnumber: 02169 103-766-2
Serial#:1321 Amount:$600.00
Serial#:1322 Amount:$539.26

"""