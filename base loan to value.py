print('''
    Calculate Base Loan amount for FHA refinance loans
    ==================================================
    ''')
#use a payoff statement from previous loan to obtian information
print('''Calculate maximum loan amount. Please enter numbers instead of characters for accurate results''')
restart = "y"
def base_model(): 
    unpaid_balance = input('''Enter Unpaid principal balance of the first mortgage:
        ''')
    unpaid_balance = float (unpaid_balance)
    
    mortgage_insurance = input('''Enter Mortgage Insurance Premium (MIP) due on the existing mortgage:
        ''')
    mortgage_insurance = float(mortgage_insurance)
   
    interest_due = input('''Enter interest due on the existing mortgage:
        ''')
    interest_due = float(interest_due)
    
    escrow_shortage = input ('''Enter escrow shortgage if applicable. If not applicable, enter 0:
        ''')
    escrow_shortage = float(escrow_shortage)

    refund_UFMIP = input('''Enter refund of UFMIP:
        ''')
    refund_UFMIP = float(refund_UFMIP)
    
    print('''      
Your Base Loan Amount:
        ''')
    print (unpaid_balance+mortgage_insurance+interest_due+escrow_shortage-refund_UFMIP)

while restart == "y":
    base_model()
    continue_question = input ('''
    Do you want to continue? Y/N: ''').lower()
    restart = continue_question
    if restart == "y":
     continue
else:
    print ('''
           Goodbye!''')
