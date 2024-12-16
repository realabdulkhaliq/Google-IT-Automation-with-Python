ls -l | less
#(... A list of files appears...)
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head

     # 7 the
     # 3 up
     # 3 spider
     # 3 and
     # 2 rain
     # 2 itsy
     # 2 climbed
     # 2 came
     # 2 bitsy
     # 1 waterspout.
