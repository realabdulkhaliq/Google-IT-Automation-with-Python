#!/bin/bash

meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder information' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    --forms-date-format='%Y-%m-%d' \
    2>/dev/null)
echo $meeting_info
