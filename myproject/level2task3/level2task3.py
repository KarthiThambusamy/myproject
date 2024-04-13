    ##_______ Password checker_______##
import re
print("____Welcome to password checker________")
print("""Your password must have
       * A lower case
       * A upper case 
       * must have numbers
       * must have special characters""")

user_password=input("Enter your password: ")
if len(user_password)<=8:
    print("Password must contain 8 character")
elif not re.search("[A-Z]",user_password):
    print("Password must contain atleast one upper letter")
elif not re.search("[a-z]",user_password):
    print("Password must contain atleast one lower letter")
elif not re.search("[0-9]",user_password):
    print("Password must contain atleast one number ")
elif not re.search("[@#$%&<>?]",user_password):
    print("Password must contain one special character")
else:
    print("strong password")


