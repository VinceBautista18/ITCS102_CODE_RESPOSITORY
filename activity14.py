age = int(input("What is your age? ----> "))     
is_employed = bool(input("do you have a job (True/False)? -----> "))
cs = int(input("What is your credit score? ----->  "))
ai = float(input("What is your annual income? -----> "))
has_collateral = bool(input("Do you have collateral (True/False)? -----> "))


base_rate = 0.0

if age >= 21 and is_employed == True:
    print("Applicant pass baseline requirements")
    if cs >= 750: 
        print("You have a high credit score")
        if ai >= 100000: #tier1
            base_rate = 4.5
            print("You have a high salary and high credit score, your interest rate is", base_rate)
        else :
            base_rate = 5.0
            print("You have a high salary and high credit score, your interest rate is", base_rate)

    if cs >= 600 and 750 :
        print("You have a Fair Credit Score", base_rate)
        if ai >= 40000 :
           if has_collateral == True:

            pass
           else : 
            pass

            base_rate = 7.0
            print("You have Fair salary and Fair Credit score, your interest rate is", base_rate)

        elif ai <= 40000:
            base_rate = 9.5
            print("Increase risk rate to", base_rate)
            print("okay salary low credit")
    if cs < 600 :
        print("Rejected : Credit score too low")

    else : 
        print("failed")
else : 
    print("Rejected : Fails baseline criteria")
        
    

