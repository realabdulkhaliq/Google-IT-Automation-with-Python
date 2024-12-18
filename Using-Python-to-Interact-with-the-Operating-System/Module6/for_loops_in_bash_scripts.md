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
