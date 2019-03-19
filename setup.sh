#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
deactivate

sudo cp pi-temperature.service /lib/systemd/system/
sudo systemctl enable pi-temperature
sudo systemctl start pi-temperature

sudo cp pi-temperature.nginx /etc/nginx/sites-available/pi-temperature
sudo ln -s /etc/nginx/sites-available/pi-temperature /etc/nginx/sites-enabled/pi-temperature
sudo systemctl restart nginx

