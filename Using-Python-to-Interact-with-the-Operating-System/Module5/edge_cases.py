#!/usr/bin/env python3

import re

# def rearrange_name(name):
#     result = re.search(r"^([\w .]*), ([\w .]*)$", name)
#     return "{} {}".format(result[2], result[1])

# Change Function to this
def rearrange_name(name):
  result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
  if result is None: # To avoid edge cases
    return ""
  return "{} {}".format(result[2], result[1])


