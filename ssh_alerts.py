"""
Just a Simple Python Telegram SSH Alert Script
"""
from datetime import datetime
import os
import sys
import settings as env
import requests
import ipinfo


TELEGRAM_API_KEY = env.TELEGRAM_API_KEY
TELEGRAM_CHAT_ROOM_ID = env.TELEGRAM_CHAT_ROOM_ID

IPINFO_KEY = env.IPINFO_KEY

HOST_IP = os.popen("hostname -I | awk '{ print $1 }'").readlines()[0].replace("\n", "")
HOST_NAME = os.popen("hostname").readlines()[0].replace("\n", "")


def main(ssh_ip):
    """The Main Function"""

    if IPINFO_KEY is not None:
        handler = ipinfo.getHandler(IPINFO_KEY)
        details = handler.getDetails(ssh_ip).details

        # print(details)

        message_to_send = f"""
        Hey,
        We have a login from {details['ip']} at {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        Host Server: {HOST_IP} ({HOST_NAME})

        I've gone ahead and tracked the IP:
        {details['ip']}
        {details['city']}, {details['region']}, {details['country']}
        {details['org']}
        {details['country_name']}
        """

    else:
        message_to_send = f"""
        Hey,
        We have a login from {ssh_ip} at {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        Host Server: {HOST_IP} ({HOST_NAME})
        """

    # print(message_to_send)

    send_message = f"""
    https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={TELEGRAM_CHAT_ROOM_ID}&text={message_to_send}
    """

    # print(requests.get(send_message, timeout=10).json())
    requests.get(send_message, timeout=10)


main(ssh_ip=sys.argv[3])
# main(ssh_ip="72.14.192.0")
