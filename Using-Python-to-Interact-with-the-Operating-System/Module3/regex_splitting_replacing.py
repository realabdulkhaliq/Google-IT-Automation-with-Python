import re
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

print("=============")
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

print("=============")
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))

print("=============")
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))

print("=============")
print(re.sub(r"([A-Z])\.\s+(\w+)", r"Ms. \2", "A. Weber and B. Bellmas have joined the team."))