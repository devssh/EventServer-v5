
gunicorn -c gunicorn.conf.py appnamegunicorn:app

#gunicorn -c gunicorn.conf.py appnamegunicorn:app &
# & runs it in background

# -c flag gives config file
# appnamegunicorn is the name of the python file. :app is the name of the variable inside the file.

# more permanent is using nohup to avoid hangup signals

# much better is using process and service with systemctl enable and systemctl start

# on mac the process is with launchd

#create com.immoguna.gunicorn.plist in ~/Library/LaunchAgents

# cd ~/Library/LaunchAgents
# replace /path/to/gunicorn.conf.py with actual path

# launchctl load ~/Library/LaunchAgents/com.immoguna.gunicorn.plist

# Verify with
# launchctl list | grep com.immoguna.gunicorn

# Stop with
# launchctl stop com.immoguna.gunicorn

# If it fails
# plutil -lint com.immoguna.gunicornsample.plist
# get the error code from launchctl
# id -u
# launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.immoguna.gunicornsample.plist
# launchctl unload ~/Library/LaunchAgents/com.immoguna.gunicorn.plist
# launchctl stop com.immoguna.gunicorn
# launchctl load ~/Library/LaunchAgents/com.immoguna.gunicorn.plist
# they like load and unload more than start stop

launchctl unload ~/Library/LaunchAgents/com.immoguna.gunicorn.plist
launchctl load ~/Library/LaunchAgents/com.immoguna.gunicorn.plist
launchctl list | grep com.immoguna.gunicorn

# status code 0 is success, 3 is failure, 1 is miscellaneous failure

