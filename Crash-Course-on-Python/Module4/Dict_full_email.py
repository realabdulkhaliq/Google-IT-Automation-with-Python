# The email_list function receives a dictionary, which contains domain names as keys, 
# and a list of users as values. Fill in the blanks to generate a list that contains 
# complete email addresses (e.g. diana.prince@gmail.com).


def email_list(domains):
	emails = []
	for names, users in domains.items():
		print(names, users)
		for user in users:
			emails.append(user + "@" + names)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))