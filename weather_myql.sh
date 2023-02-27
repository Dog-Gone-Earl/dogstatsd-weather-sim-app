#!/usr/bin/env bash

#sudo mysql
#CREATE DATABASE weather_stats;
#use weather_stats;
#CREATE TABLE weather_data (temp INT(3), humidity INT(3), pressure INT(3));
#show tables;
#describe weather_data;
#use weather_stats;
#CREATE USER 'DD_TESTER'@'localhost' IDENTIFIED BY 'Datadog2023';
#GRANT ALL PRIVILEGES ON *.* TO 'DD_TESTER'@'localhost';
#FLUSH PRIVILEGES;

echo "Updates! Updates! Updates!"
sleep 3
sudo apt-get update -y && sudo apt-get upgrade -y

echo "Installing pip and datadog"
sleep 5
sudo apt install python3-pip -y
pip3 install datadog

echo "mysql install"
sudo apt install mysql-server -y
pip install mysql-connector-python

echo "Retrieving Python file"
sleep 5
curl -o weather.py https://raw.githubusercontent.com/Dog-Gone-Earl/dogstatsd-weather-sim-app/main/weather_code.py
