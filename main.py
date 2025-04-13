import os
import re
import json
import smtplib
from getpass import getpass


def check_credentials(email: str, password: str) -> bool:
    """Checks if the provided credentials are valid
  

    Args:
        email (str): Valid Email Address
        password (str): Password to validate

    Returns:
        bool: Returns True if valid, False otherwise.
    """
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.quit()
    
    except Exception as ex:
        print(f"Error during login: {ex}")
        return False
        


def validate_email_format(email: str) -> bool:
    """Validates the format of an email address using a regular expression.

    Args:
        email (str): Email Address to validate

    Returns:
        bool: Returns True if valid else False
    """
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def take_inputs():

    print("Enter Sender Email and Password")
    sender_email = input("Email Address : ")

    if not validate_email_format(sender_email):
        print(f"Invalid Email Address : {sender_email}")
        exit(1)

    sender_password = getpass("Password : ")
    if not check_credentials(sender_email, sender_password):
        exit(1)
      
    data = {"sender_email": sender_email, "sender_password": sender_password}
    
    path = input("Enter Path to Recipients data in JSON Format : ")
    if not os.path.exists(path):
        print(f"Path doesn't exist : {path}")
        exit(1)
        
    with open(path, 'r') as file:
        recipients_data = json.load(file)
    
    data["recipients"] = recipients_data
    
    return data



if __name__ == "__main__":
    
    emails_data = take_inputs()