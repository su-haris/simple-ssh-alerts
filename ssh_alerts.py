"""
Just a Simple Python Telegram SSH Alert Script
"""
from datetime import datetime
import time
import os
import sys
import json
import settings as env
import urllib.request, urllib.parse

TELEGRAM_API_KEY = env.TELEGRAM_API_KEY
TELEGRAM_CHAT_ROOM_ID = env.TELEGRAM_CHAT_ROOM_ID
WHITELIST_IP = env.WHITELIST_IP

HOST_IP = os.popen("hostname -I | awk '{ print $1 }'").readlines()[0].replace("\n", "")
HOST_NAME = os.popen("hostname").readlines()[0].replace("\n", "")

IP_API_SITE = "http://ip-api.com/json/"


def main(ssh_ip):
    """The Main Function"""
    details = None
    current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    current_tz = time.strftime("%Z", time.localtime())

    if ssh_ip == "INSTALLER_SSH":
        message_to_send = "Installation of simple-ssh-alerts is successful!"
    else:
        if ssh_ip in WHITELIST_IP:
            exit("Whitelisted IP, not sending login alert.")
            
        try:
            details = urllib.request.urlopen(IP_API_SITE + ssh_ip)
            details = details.read()
            details = json.loads(details.decode("utf-8"))
        except Exception as e:
            print("Exception while trying to call IP API", e)

        if details and details["status"] == "success":
            message_to_send = f"""
            Hey,
            We have a login from {details['query']} at {current_datetime} {current_tz}
            Host Server: {HOST_IP} ({HOST_NAME})

            Connection IP:
            {details.get('query')}
            {details.get('city', 'Unknown')}, {details.get('regionName', 'Unknown')}, {details.get('country','Unknown')}
            {details.get('isp', 'Unknown ISP')} ({details.get('as', 'Unknown')})
            """
        else:
            message_to_send = f"""
            Hey,
            We have a login from {ssh_ip} at {current_datetime} {current_tz}
            Host Server: {HOST_IP} ({HOST_NAME})
            """

    message_to_send_encoded = urllib.parse.quote(message_to_send)
    send_message = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={TELEGRAM_CHAT_ROOM_ID}&text={message_to_send_encoded}"

    urllib.request.urlopen(send_message)


main(ssh_ip=sys.argv[1])
# main(ssh_ip="72.14.192.0")
