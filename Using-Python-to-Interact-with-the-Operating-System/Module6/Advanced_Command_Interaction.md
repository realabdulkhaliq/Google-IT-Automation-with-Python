tail /var/log/syslog

Code output:

May 24 10:17:01 ubuntu.local CRON[257236]: (root) CMD ( cd / && run-parts --report /etc/cron.hourly)

May 24 10:18:41 ubuntu.local rsyslogd: -- MARK --

May 24 10:25:19 ubuntu.local systemd[1]: Reloading.

tail /var/log/syslog | cut -d' ' -f5-

Code output:

CRON[257236]: (root) CMD ( cd / && run-parts --report /etc/cron.hourly)

rsyslogd: -- MARK --

systemd[1]: Reloading.

cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head

#!/bin/bash

for logfile in /var/log/\*log; do
echo "Processing: $logfile"
cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done

About this code
This script is written in the Bash scripting language and designed to analyze log files. It analyzes each log file in the /var/log directory and displays the top 5 most frequently occurring messages along with their counts.

./toploglines.sh
