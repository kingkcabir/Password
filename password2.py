
import string
import random

def password_setter(lenght, Password):
        #setting the pattern      
        characts = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        #generating password
        gen_password = "".join(random.choices(characts, k=lenght))

        print(f"Password must be in '{gen_password}' format and must be {lenght} characters long")
        print("Set your password!")

        #special characters
        special_characters = "!@#$%^&()?_,<>/.{[]}/\|-+="
        #small letters
        small_letters = "abcdefghijklmnopqrstuvwxyz"
        #capital letters
        capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #numbers
        numeric = "0123456789"
        #setting password
        Password = "".join(input("Set Password: "))

        while Password:
                if len(Password) < lenght or len(Password) > lenght:
                        print(f"Password must be {lenght} characters long")
                
                elif not any(c in special_characters for c in Password):
                        print('Password must contain special characters')
                        
                elif not any(i in small_letters for i in Password):
                        print('Password must contain small letters')
                        
                elif not any(j in capital_letters for j in Password):
                        print('Password must contain capital letters')
                        
                elif not any(t in numeric for t in Password):
                        print('Password must contain numeric figures')
                
                else:
                        print(f"Password {Password} set successfully")
                
                
                break        
        
print(password_setter(20, 'Password'))