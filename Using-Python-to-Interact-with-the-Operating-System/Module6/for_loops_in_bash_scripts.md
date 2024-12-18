#!/bin/bash

for fruit in peach orange pear; do

        echo "I like $fruit!"

done

cd old_website/
/old_website$ ls -l

/old_website$ basename index.HTM .HTM

#!/bin/bash

for file in \*.HTM; do
name=$(basename "$file" .HTM)
mv "$file" "$name.html"
done

#!/bin/bash

for file in \*.HTM; do
name=$(basename "$file" .HTM)
echo mv "$file" "$name.html"
done

The script iterates through all files with the ".HTM" extension in the current directory. For each file, it extracts the filename without the extension and generates the new filename with the ".html" extension. Finally, it prints the mv command that would rename the original file to the new filename.

Note: This script only prints the mv commands. To actually rename the files, you need to execute the script by running chmod +x script.sh && ./script.sh where script.sh is the name of the script file.

/old_website$ chmod +x rename.sh
/old_website$ ./rename.sh

/old_website$ ./rename.sh
/old_website$
/old_website$ ls -l

ls -l
