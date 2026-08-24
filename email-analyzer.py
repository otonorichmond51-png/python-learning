email = input("Enter your email: ")
cleaned_email = email.strip().lower()
parts = cleaned_email.split("@")
username = parts[0]
domain = parts[1]
print("Email:", cleaned_email)
print("Username:", username)
print("Domain:", domain)