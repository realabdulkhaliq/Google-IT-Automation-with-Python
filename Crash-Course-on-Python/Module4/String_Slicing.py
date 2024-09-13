# String Indexing

fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])

text = "Random string with a lot of characters"
print(text[-1])
print(text[-2])


message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)


def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:     # Concatination is in string or not
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email