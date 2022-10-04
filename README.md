# crontab

1. Set up and start virtual machine
2. ssh user@public_ip
3. Password
4. sudo apt-get update
5. select-editor --> 1 for nano
6. git clone url
7. cd into folder
8. crontab -e --> add cron expression <br>
    ex. * * * * * usr/bin/python3 pwd path
9. Notes: <br>
    sudo service cron reload (to restart) <br>
    systemctl status cron (status)

# Execute file once a day
23 16 * * * /usr/bin/python3 /home/rima/crontab/crontab.py

# Execute file every Sunday at 10pm
0 20 * * SUN /usr/bin/python3 /home/rima/crontab/crontab.py

# Execute file at the end of every quarter
0 0 1 */3 * /usr/bin/python3 /home/rima/crontab/crontab.py
