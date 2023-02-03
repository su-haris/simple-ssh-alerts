#!/bin/bash

# Check if python is installed
if command -v python3 &>/dev/null; then
  echo "Python3 is installed."
else
  echo "Python3 is not installed."

  # Check the distribution
  if [ -f /etc/redhat-release ]; then
    # Install Python3 on Redhat/CentOS
    sudo yum install python3 -yq
  elif [ -f /etc/lsb-release ]; then
    # Install Python3 on Ubuntu/Debian
    sudo apt-get update -q
    sudo apt-get install python3 -yq
  elif [ -f /etc/os-release ]; then
    source /etc/os-release
    if [ "$ID" == "amzn" ]; then
      # Install Python3 on Amazon Linux
      sudo yum install python3 -yq
    fi
  else
    echo "Distribution not supported."
    echo "Try to install Python3 manually and try again."
    exit 1
  fi
fi

REPO_URL="https://github.com/su-haris/simple-ssh-alerts.git"

# Clone the repository
git clone $REPO_URL
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

CURRENT_DIR=$(pwd)

#!/bin/bash

current_directory=$(pwd)

echo "if [ -n \"\$SSH_CLIENT\" ]; then
  python3 $CURRENT_DIR/ssh_alerts.py \$SSH_CLIENT
fi" | sudo cat >> /etc/profile

echo "Installation of simple-ssh-alert is complete."