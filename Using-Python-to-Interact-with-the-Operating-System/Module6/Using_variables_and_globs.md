Setting Variable

example=hello

echo $example

Code output:

hello

example = hello

Code output:

Command ‘example’ not found, did you mean:

    Command ‘gexample’ from deb pvm-examples (3.4.6-2build1)

Try: sudo apt install <deb name>

Spaces are not allowed

#!/bin/bash

line="-------------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"

./gather-information.sh

echo \*.py
