# simple-ssh-alerts
A Simple SSH Alert Script based on Python+Telegram. <br>
Get notified on Telegram for every SSH connection made to your Linux machine! <br>
Uses Python3 and its inbuilt libraries so need of any external libs.<br>

## Installation
```
wget https://raw.githubusercontent.com/su-haris/simple-ssh-alerts/master/installer.sh -O ssa-installer.sh && bash ssa-installer.sh
```
Follow the on screen instructions to finish the setup

## Sample Alert on Telegram
```
Hey,
We have a login from 1.1.1.1 at 04/02/2023 17:00:41 UTC
Host Server: 8.8.8.8 (my-awesome-server)

Connection IP:
1.1.1.1
Los Angeles, California, United States
Cloudflare, Inc. (AS13335 Cloudflare, Inc.)
```

```
Hey,
We have a login from 8.8.8.8 at 04/02/2023 17:02:41 UTC
Host Server: 1.1.1.1 (my-gaming-server)
```

## Future Plans
- ~~Add one click installer along with virtualenv and requirements setup~~
- Add email support (Maybe)
- Add whitelist countries and IPs
- Add silent notifications to Telegram
