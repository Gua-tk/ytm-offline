# ytm-offline
Program to download and reupload music from youtube videos, so you can lock your phone while listening to youtube music for free.


### Usage 
```shell
cd ytm-offline
python3 -m venv venv
venv/bin/python3 -m pip install --upgrade pip
venv/bin/python3 -m pip install -r requirements.txt
venv/bin/python3 src/main.py
```

### Docker Usage
```shell
sudo docker build -t axlfc/ytm-offline:latest . &&  sudo docker push axlfc/ytm-offline:latest && sudo docker-compose down && sudo docker-compose up -d
```


sudo docker compose up -d