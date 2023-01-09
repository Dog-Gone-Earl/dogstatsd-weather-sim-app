#!/usr/bin/env bash

echo "Updates! Updates! Updates!"
sudo apt-get update -y && sudo apt-get upgrade -y

echo "Installing pip and datadog"
sudo apt install python3-pip
pip3 install datadog

echo "Retrieving Python file"
eval "$(https://raw.githubusercontent.com/Dog-Gone-Earl/dogstatsd-weather-sim-app/main/weather_code.py)"
