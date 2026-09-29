age = int(input("Age -----> "))
rev = float(input("Revenue -----> "))
cc = int(input("Credit Score -------> "))
years = float(input("Years of Business ----> "))
has_defaults = bool(input("File for Bankruptcy --------->"))
collateral = input("Collateral name ------> ")
c_value = float(input("Collateral Value ------> "))

max_loan = 0
base_fee = 0

if age >= 21 and years >= 2.0 and has_defaults == False:
    print("Baseline Passed")
    if cc >= 720:
        max_loan = rev * 3
        print("Maximum Loanable amount is set to", max_loan)
        print("High Credit Score")
        if rev >= 50000:
            print("Revenue higher than 50000")
            base_fee = max_loan * 0.015
            print("Base fee rate is set to", base_fee)
        else:
            print("Revenue Lower than 50000")
            base_fee = max_loan * 0.025
            print("Base fee rate is set to", base_fee)
        if c_value >= max_loan:
            print("Collateral", collateral," with a value of ", c_value, " is Accepted")
        else:
            print("Rejected: Insufficient collateral value for ", collateral)

        surge_fee_rate = max_loan * base_fee
        if max_loan % 500 != 0:
            print("Additional Charge added")
            surge_fee_rate += 250
            print("Updated base fee is", surge_fee_rate)        

    elif cc >= 620 and cc < 720:   
        print("Credit score within range of 620 to 720")
        max_loan = rev * 1.5
        print("Maximum loan for this credit score is", max_loan)
        if years >= 5:
            print("Business Years")
            base_fee = max_loan * 0.02
            print("Base fee rate is set to", base_fee)
        else:
            print("Business year less than 5 years")
            base_fee = max_loan * 0.035
            print("Base fee rate is set to", base_fee)

        if c_value >= max_loan:
            print("Collateral", collateral," with a value of ", c_value, " is Accepted")
        else:
                print("Rejected: Insufficient collateral value for ", collateral)
            
        surge_fee_rate = max_loan * base_fee
        if max_loan % 500 != 0:
            print("Additional Charge added")
            surge_fee_rate += 250
            print("Updated base fee is", surge_fee_rate)        
    elif cc < 620 and cc >= 1:
        print("Credit Score too low") 

    else:
        print("INVALID")

else:
    print("Baseline Failed")



