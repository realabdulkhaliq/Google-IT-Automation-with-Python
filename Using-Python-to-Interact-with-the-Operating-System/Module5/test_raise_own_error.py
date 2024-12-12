from try_except_raise_own_error import validate_user

validate_user("", -1)   # give error
validate_user("", 1)
validate_user("myuser", 1)
validate_user(88, 1)    # error
validate_user([], 1)
validate_user(["name"], 1)  # error
