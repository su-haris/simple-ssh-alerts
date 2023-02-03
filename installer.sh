#!/bin/bash
# Installer Script for simple-ssh-alerts
# A Simple SSH Alert Script based on Python+Telegram
# https://github.com/su-haris/simple-ssh-alerts

REPO_URL="https://github.com/su-haris/simple-ssh-alerts.git"
CURRENT_DIR=$(pwd)

echo "Installing simple-ssh-alerts"
echo -e

# Check if python is installed
echo "Checking for Python Installation"

if command -v python3 &>/dev/null; then
  echo "Python3 is installed."
else
  echo "Python3 is not installed."
  echo "Proceeding to install Python3."

  # Check the distribution
  if [ -f /etc/redhat-release ]; then
    # Install Python3 on Redhat/CentOS
    yum install python3 -yq
  elif [ -f /etc/lsb-release ]; then
    # Install Python3 on Ubuntu/Debian
    apt-get update -q
    apt-get install python3 -yq
  elif [ -f /etc/os-release ]; then
    source /etc/os-release
    if [ "$ID" == "amzn" ]; then
      # Install Python3 on Amazon Linux
      yum install python3 -yq
    fi
  else
    echo "Distribution not supported."
    echo "Try to install Python3 manually and try again."
    exit 1
  fi
  echo "Python3 is successfully installed!"
  echo -e
fi

# Clone the repository
echo "Cloning repository for the necessary files."
echo -e
git clone -q $REPO_URL
cd simple-ssh-alerts

# Ask the user to input the TELEGRAM_API_KEY
echo "Enter your TELEGRAM_API_KEY: "
read TELEGRAM_API_KEY

# Ask the user to input the TELEGRAM_CHAT_ROOM_ID
echo "Enter your TELEGRAM_CHAT_ROOM_ID: "
read TELEGRAM_CHAT_ROOM_ID

# Write the values to the file
echo "TELEGRAM_API_KEY = '$TELEGRAM_API_KEY'" > settings.py
echo "TELEGRAM_CHAT_ROOM_ID = '$TELEGRAM_CHAT_ROOM_ID'" >> settings.py

# Confirm that the values have been written to the file
echo "Values written to settings.py"

# Update /etc/profile to trigger script on SSH
echo "if [ -n \"\$SSH_CLIENT\" ]; then
  python3 $CURRENT_DIR/ssh_alerts.py \$SSH_CLIENT
fi" | cat >> /etc/profile

# Send a test notification to Telegram to confirm installation works.
python3 "$CURRENT_DIR/ssh_alerts.py" "INSTALLER_SSH"

echo "Installation of simple-ssh-alert is complete."
echo "You should have recieved a notification on Telegram if installation was successful."