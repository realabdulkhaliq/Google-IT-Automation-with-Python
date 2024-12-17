cat check_localhost.sh

About this code
Here we’ll start with the if keyword, followed by the grep command. This is how we’ll check for success. At the end of the command, we have a semicolon [;], followed by the word then. After that comes the body of the conditional.

Code output:

#!/bin/bash

if grep "127\.0\.0\.1" /etc/hosts; then

    echo "Everything ok"

else

    echo "ERROR! 127.0.0.1 is not in /etc/hosts"

fi

./check_localhost.sh

Code output:

127.0.0.1 localhost

Everything ok

if test -n "$PATH"; then echo "Your path is not empty"; fi

Code output:

Your path is not empty

if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

Code output:

Your path is not empty
