## Email Validator ##

def validate_email(email):
    symbol=False
    dot=True
    for i in email:
        if i=="@":
            symbol= True
        elif i==".":
            dot=True
        elif " " in email:
            return False
    return symbol and dot
email=input("Enter your email: ")
if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")
