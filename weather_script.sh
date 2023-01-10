#!/usr/bin/env bash

echo "Updates! Updates! Updates!"
sleep 3
sudo apt-get update -y && sudo apt-get upgrade -y

echo "Installing pip and datadog"
sleep 5
sudo apt install python3-pip
pip3 install datadog

echo "Retrieving Python file"
sleep 5
curl -0 https://raw.githubusercontent.com/Dog-Gone-Earl/dogstatsd-weather-sim-app/main/weather_code.py
