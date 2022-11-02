# simple-ssh-alerts (Work In Progress)
A Simple SSH Alert Script based on Python+Telegram

**Detailed Instructions to be added soon!**

This simple script is a work in progress which alerts you on telegram.
If you have IPInfo access key, it fetches info of source IP.

## Future Plans
- Add one click installer along with virtualenv and requirements setup
- Add email support
- Add whitelist countries
- Add silent notifications to telegram

## Installation
- git clone https://github.com/su-haris/simple-ssh-alerts.git
- pip install ipinfo (crude way, will be changed soon)
- Modify settings.py with appropriate values (crude way, will be changed soon)
- Add the following lines to /etc/profile
  ```
  if [ -n "$SSH_CLIENT" ]; then
    python3 simple-ssh-alerts/ssh_alerts.py echo $SSH_CLIENT
  fi
  ```
