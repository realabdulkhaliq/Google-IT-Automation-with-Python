# mkdir mynewdir
# cd mynewdir/
# /mynewdir$ pwd
# /mynewdir$ cp ../spider.txt .
# /mynewdir$ touch myfile.txt
# /mynewdir$ ls -l 
# #Output:
# #-rw-rw-r-- 1 user user   0 Mai 22 14:22 myfile.txt
# #-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
# /mynewdir$ ls -la
# #Output:
# #total 12
# #drwxr-xr-x  2 user user  4096 Mai 22 14:17 .
# #drwxr-xr-x 56 user user 12288 Mai 22 14:17 ..
# #-rw-rw-r--  1 user user     0 Mai 22 14:22 myfile.txt
# #-rw-rw-r--  1 user user   192 Mai 22 14:18 spider.txt
