#!/usr/bin/env bash


echo "Installing pip and datadog"
sleep 5
sudo apt install python3-pip -y
pip3 install datadog

echo "Retrieving Python file"
sleep 5
curl -o weather.py https://raw.githubusercontent.com/Dog-Gone-Earl/dogstatsd-weather-sim-app/main/weather_code.py
