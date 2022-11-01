"""
Just a Simple Python Telegram SSH Alert Script
"""
from datetime import datetime
import os
import sys
import requests
import ipinfo


TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY", "INSERT-KEY-HERE")
TELEGRAM_CHAT_ROOM_ID = os.getenv("TELEGRAM_CHAT_ROOM_ID", "INSERT-KEY-HERE")

IPINFO_KEY = os.getenv("IPINFO_KEY", "INSERT-KEY-HERE")


def main(ssh_ip, host_ip):
    """The Main Function"""

    if IPINFO_KEY is not None:
        handler = ipinfo.getHandler(IPINFO_KEY)
        details = handler.getDetails(ssh_ip).details

        # print(details)

        message_to_send = f"""
        Hey,
        We have a login from {details['ip']} at {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        Host Server: {host_ip}

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
        Host Server: {host_ip}
        """

    # print(message_to_send)

    send_message = f"""
    https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={TELEGRAM_CHAT_ROOM_ID}&text={message_to_send}
    """

    # print(requests.get(send_message, timeout=10).json())
    requests.get(send_message, timeout=10)


main(ssh_ip=sys.argv[3], host_ip=sys.argv[2])
# main(ssh_ip="72.14.192.0", host_ip="localhost")
