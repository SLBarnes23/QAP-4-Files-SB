# Program to calculate new insurance policy
#Information for its customers
# Date written: November 19th - November 24th 
# Author: Steve Barnes

import datetime
from prettytable import PrettyTable
import re

# Constants
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
ADD_CAR_DISCOUNT = 0.25
EXTRA_LIABILITY = 130.00
GLASS_COVERAGE = 86.00
LOANER_CAR_COVERAGE = 58.00
HST_RATE = 0.15
PROCESSING_FEE_MTLY_PYMTS = 39.99

#Define functions used in my program

# Function to validate phone number format
def is_valid_phone_number(phone_number):
    return re.match(r'^\d{10}$', phone_number) is not None

# Function to validate postal code format
def is_valid_postal_code(postal_code):
    return re.match(r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$', postal_code) is not None

# Function to format dollars
def FDollar2(DollarValue):
    return "${:,.2f}".format(DollarValue)

# Function to calculate premium
def calculate_premium(NumCars):
    InitialPremium = 869.00
    DiscountPercentage = 25

    if NumCars == 1:
        return InitialPremium
    else:
        Discount = (DiscountPercentage / 100) * InitialPremium
        DiscountedPremium = InitialPremium - Discount
        return DiscountedPremium + (DiscountedPremium * (NumCars - 1))

# Create a PrettyTable instance for the claims table
claims_table = PrettyTable()
claims_table.field_names = ["Claim #", "Date", "Cost"]

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

# Function fo inputting old claims
def input_claims():
    global claims_table  # Declare claims_table as global
    claims = []
    for i in range(1, 4):
        date = input(f"Please enter the date of the {ordinal(i)} claim (YYYY-MM-DD): ")
        cost = float(input(f"Please enter the cost of the {ordinal(i)} claim: "))
        claims_table.add_row([i, date, FDollar2(cost)])
        claims.extend([date, cost])
    return claims



 # Function to calculate extra costs
def calculate_extra_costs(num_cars, extra_liability, glass_coverage, loan_car):
    # Function to calculate extra costs
    extra_liability_cost = 130.00 * num_cars if extra_liability == 'Y' else 0.00
    glass_coverage_cost = 86.00 * num_cars if glass_coverage == 'Y' else 0.00
    loan_car_cost = 58.00 * num_cars if loan_car == 'Y' else 0.00
    return extra_liability_cost, glass_coverage_cost, loan_car_cost


while True:
# User Inputs
    CustFName = input("Please enter the customer's first name: ").title()
    CustLName = input("Please enter the customer's last name: ").title()
    CustAdd = input("Please enter the customer's address: ")
    CustCity = input("Please enter the customer's city: ").title()

    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BS", "YT", "NT", "NV"]
    while True:
        CustProv = input("Please enter the customer's province (XX): ").upper()
        if CustProv == "" or len(CustProv) != 2 or CustProv not in ProvLst:
            print("Error - Please enter a valid province.")
        else:
            break

    while True:
        CustPost = input("Please enter the customer's postal code: ").upper()
        if is_valid_postal_code(CustPost):
            break
        else:
            print("Error - Please enter a valid postal code (e.g., A1B 2C3).")


    while True:
        CustPhoneNum = input("Please enter customer's phone number (9999999999): ")
        if is_valid_phone_number(CustPhoneNum):
            break
        else:
            print("Error - Please enter a valid phone number (10 digits).")

    NumCars = int(input("Please enter the number of cars being insured: "))
    TotalPremium = calculate_premium(NumCars)
    ExtraLiability = input("Does the customer want extra liability up to $1,000,000? (Y/N): ").upper()
    GlassCov = input("Does the customer require option glass coverage? (Y/N): ").upper()
    LoanCar = input("Does the customer want the loaner car option? (Y/N): ").upper()



# Claim Inputs
    ClaimLst = input_claims()


# Calculate Extra Liability Cost
    ExtraLiabilityCost = 130.00 * NumCars if ExtraLiability == 'Y' else 0.00

# Calculate Glass Coverage Cost
    GlassCovCost = 86.00 * NumCars if GlassCov == 'Y' else 0.00

# Calculate Loaner Car Cost
    LoanCarCost = 58.00 * NumCars if LoanCar == 'Y' else 0.00

# Calculate Total Extra Cost
    TotalExtraCost = ExtraLiabilityCost + GlassCovCost + LoanCarCost

    InsPrem = BASIC_PREMIUM + (BASIC_PREMIUM * NumCars) - (.25 * BASIC_PREMIUM * (NumCars - 1))

    DownpayAmount = 0 #Initialize dowwn payment amount
# Calculations
    TotalInsPrem = InsPrem + TotalExtraCost - DownpayAmount
    Hst = TotalInsPrem * HST_RATE
    TotalCost = TotalInsPrem + Hst




# Payment Input
    PayLst = ["Full", "Monthly", "Down Pay"]
    DownpayAmount = 0 #Initialize dowwn payment amount
    ProcessingFee = 39.99

    while True:
        Payment = input("Does the customer wish to pay in full, monthly, or down pay?: ").title()
        if Payment == "" or Payment not in PayLst:
            print("Error - Please enter a valid payment option.")
        elif Payment == "Down Pay":
            DownpayAmount = float(input("Please input the Downpayment amount: "))
            break
        elif Payment == "Full" or Payment == "Monthly":
            break

# Calculate total cost based on user selection

    TotalCost = TotalInsPrem

    if Payment == "Monthly":
        TotalCost += ProcessingFee  # Include processing fee for monthly payment

    if Payment == "Down Pay":
        TotalCost -= DownpayAmount  # Subtract down payment if applicable
        TotalCost += ProcessingFee  # Include processing fee for down payment

# Calculate monthly payment
    if Payment == "Full":
        MonthlyPay = 0  # No monthly payment if paying in full
        PaymentOption = "Full"
    elif Payment == "Monthly":
        MonthlyPay = TotalCost / 8
        PaymentOption = f"Monthly (with a down payment of ${DownpayAmount:.2f})"
    else:  # Assuming it's the "Down Pay" option
        MonthlyPay = (TotalCost - ProcessingFee) / 8
        PaymentOption = f"Monthly with down payment of ${DownpayAmount:.2f}"




    TotalInsPrem = InsPrem + TotalExtraCost - DownpayAmount
    TotalCost = TotalInsPrem + Hst

# Calculate  Payment

# Calculate Monthly Payment
    if Payment == "Monthly":
        if DownpayAmount > 0:
            MonthlyPay = (TotalCost - DownpayAmount) / 8
        else:
            MonthlyPay = TotalCost / 8
    elif Payment == "Full":
        MonthlyPay = 0
    else:
        MonthlyPay = None  # Set a default value if Payment is not "Monthly"

# Determine payment information
    if Payment == "Down Pay":
        payment_info = f"Down Payment Amount: {FDollar2(DownpayAmount)}"
    elif Payment == "Monthly":
        payment_info = f"Monthly Payment Amount: {FDollar2(MonthlyPay)}"
    elif Payment == "Full":
        payment_info = f"Full Payment Amount: {FDollar2(TotalCost)}"
    else:
        payment_info = "Invalid Payment Option"

    CurDate = datetime.datetime.now()
    first_day_next_month = datetime.datetime(CurDate.year, CurDate.month % 12 + 1, 1)


    InsPrem = BASIC_PREMIUM + (BASIC_PREMIUM * NumCars) - (.25 * BASIC_PREMIUM * (NumCars - 1))

    TotalExtraCost = ExtraLiabilityCost + GlassCovCost + LoanCarCost

# Output of receipt/invoice

    print("\nOne Stop Insurance Company                    Invoice Date:", CurDate.strftime('%B %d, %Y'))
    print("Insurance Policy Information                  First Payment Date:", first_day_next_month.strftime('%B %d, %Y'))

    PolicyNum = CustFName[0] + CustLName[0] + "-" + CustPost[3:6] + "-" + CustPhoneNum[6:]
    print(f"Policy No: {PolicyNum} \n\n\n\n")
    print(f"Customer Name: {CustFName} {CustLName} ({CustPhoneNum})\n")
    print(f"""Address:       {CustAdd}
                            {CustCity} {CustProv}
                            {CustPost}""")
    print("---------------------------------------------------------\n")
    print("Insurance Details\n-------------------\n")
    print(f"Number of Cars: {NumCars}")

# Extra Liability
    print(f"Extra Liability?: {'Yes' if ExtraLiability == 'Y' else 'No'}         Extra Liability Cost: {FDollar2(ExtraLiabilityCost):>20}")

# Glass Coverage
    print(f"Glass Coverage?: {'Yes' if GlassCov == 'Y' else 'No'}          Glass Coverage Cost: {FDollar2(GlassCovCost):>21}")

# Loaner Car
    print(f"Loaner Car?: {'Yes' if LoanCar == 'Y' else 'No'}              Loaner Car Cost: {FDollar2(LoanCarCost):>25}")
    print()
    print(f"                              --------------------------------------------- ")
    print()
    print(f"                              Total Extra Costs: {FDollar2(TotalExtraCost):>24}   ")
    print()
    print()
    print (f"                              Payment")
    print(f"                              ---------------------------------------------")
    print()
    print(f"                              Payment Option: {PaymentOption}")  
    print("")
    print(f"                              Insurance Premium: {FDollar2(InsPrem):>24}")
    print(f"                              Total Extra Costs: {FDollar2(TotalExtraCost):>24}")
    print(f"                              Down Payment Amount: {FDollar2(DownpayAmount):>22}")
    print (f"                              Total Insurance Premium: {FDollar2(TotalInsPrem):>18}")
    print (f"                              HST: {FDollar2(Hst):>38} ")
    print(f"                              -------------------------------------------")
    print()
    print (f"                             Total Cost: {FDollar2(TotalCost):>32}      ")
    print()
    print()
    print(f"Past Claims")
    print()
    print(claims_table)