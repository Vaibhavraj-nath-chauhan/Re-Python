email = input("Enter email address:-")
user = email[:email.index("@")]
domain = email[email.index('@')+1:]
print(user)
print(domain)