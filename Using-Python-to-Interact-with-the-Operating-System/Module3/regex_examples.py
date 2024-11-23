import re
result = re.search(r"aza", "plaza")
print(result)

result1 = re.search(r"aza", "bazaar")
print(result1)

result2 = re.search(r"aza", "maze")
print(result2)

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))