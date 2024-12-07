import subprocess
subprocess.run(["cmd", "/c", "date /T"])

from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

subprocess.run(["timeout", "/T", "2", "/NOBREAK"])

import time
time.sleep(2)  # Pause for 2 seconds
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))