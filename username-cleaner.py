original = input("Enter username: ")
cleaned_username = original.strip().lower()
length = len(cleaned_username)
contains_admin = "admin" in cleaned_username
print("Original:", original)
print("Cleaned:", cleaned_username)
print("Length:", length)
print("Contains admin:", contains_admin)

