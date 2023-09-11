# ytm-offline

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fd11bee5a7b4412a93a13b46dfbee2fa)](https://app.codacy.com/gh/ytm-manager/ytm-manager-backend?utm_source=github.com&utm_medium=referral&utm_content=ytm-manager/ytm-manager-backend&utm_campaign=Badge_Grade)

Program to download and reupload music from youtube videos, so you can lock your phone while listening to youtube music for free.

### TODO:
- [ ] Implement an end point that receives mp3 and upload to ytmusic.
- [ ] Implement an end point that receives a zip of .mp3 files to upload them to yt music.
- [ ] Change implementation of getting the current directory in APIController do it as in the upload service.
- [x] Add flexibility with the usage of the two different type of secrets.
- [ ] Read authentication for youtube music in each request instead of retrieving it from secrets.
- [x] Fix the docker network reachment. Port 5000 working without Docker.
- [ ] UploadPlaylist create a playlist in youtube music, download it an and add to the playlists in yt music playlists.

### TODO ?
- [ ] FRONTEND: Make API requests in Flutter
- [x] Show Text in App
- [x] TextBox Input (URL, FILE_PATH)
- [ ] Open File Button
- [ ] SendFile Button
- [ ] Refresh Session text box input widget


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
sudo docker build -t aleixmt/ytm-offline:latest . &&  sudo docker push aleixmt/ytm-offline:latest && sudo docker-compose down && sudo docker-compose up -d
```


sudo docker compose up -d

### Example of playlist
https://youtube.com/playlist?list=PLvEI0iOxif017-fv4P0ApFmzRI-vWBPvb&si=BmAWXxAFVAa_gg86
