#!/bin/bash

if ! command -v google-chrome &> /dev/null
then
    echo "Installing Google Chrome"

    sudo apt update
    sudo apt install -y wget curl gnupg
    wget https://mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.90-1_amd64.deb
    sudo dpkg -i google-chrome-stable_114.0.5735.90-1_amd64.deb
    sudo apt install -f -y

    echo "Google Chrome installed successfully"
else
    echo "Google Chrome already installed"
fi
