# get user email address
email = input("email address:").strip()

# slice out user name
name = email[: email.index("@")]
print(name)

# slice domain name
domain = email[(email.index("@") + 1):]
print(domain)

# format message
output = "Your username is {} and your domain name is {}".format(name, domain)
print(output)