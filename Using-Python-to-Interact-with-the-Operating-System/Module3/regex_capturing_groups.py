import re
# result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
# print(result)
# print(result.groups())
# print(result[0])
# print(result[1])
# print(result[2])
# "{} {}".format(result[2], result[1])

# print("=============")

# print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))

# print(re.search(r"^(\w*), (\w*)$", "Lovelace, Ada"))
# print(re.search(r"^(\w*), (\w*)$", "Lovelace, Ada").groups())
# print(re.search(r"^(\w*), (\w*)$", "Lovelace, Ada").group(0))
# print(re.search(r"^(\w*), (\w*)$", "Lovelace, Ada").group(1))
# print(re.search(r"^(\w*), (\w*)$", "Lovelace, Ada").group(2))

# print("=============")

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")

# rearrange_name("Ritchie, Dennis")

# print("=============")

# def rearrange_name(name):
#     result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
#     if result == None:
#         return name
#     return "{} {}".format(result[2], result[1])
# rearrange_name("Hopper, Grace M.")