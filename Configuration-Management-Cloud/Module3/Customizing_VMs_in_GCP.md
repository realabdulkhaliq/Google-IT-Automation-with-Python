```
git clone https://github.com/blue-kale/hello
cd hello
ls -l
./hello_cloud.py

```

The first line of this code uses the git clone command to clone the github repository blue-kale/hello. The second line uses the cd command to change the directory to this new directory, hello. The third line uses the ls command to list the files in the hello directory. This directory includes a simple web-serving application written in Python, called hello_cloud.py. The last line of code runs this application, which causes a socket to open and listen for HTTP connections on port 8000.

```
sudo ./hello_cloud.py 80
```

The sudo command allows us to pass a different port, port 80, to the hello_cloud.py application so it listens on port 80 instead of on port 8000.

```
cat hello_cloud.service
```

This code opens the service definition file, also called a systemd file, for the hello_cloud.py application.
