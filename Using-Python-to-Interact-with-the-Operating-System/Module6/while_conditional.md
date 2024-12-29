#!/bin/bash

n=1
while [ $n -le 5 ]; do
echo "Iteration number $n"
((n+=1))
done

./while.sh

cat while.sh

Code output:

#!/usr/bin/env python

import random

value=random.randint(0, 3)

print("Returning: " + str(value))

sys.exit(value)

./random-exit.py
