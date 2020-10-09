# Telegram-Leech-Bot

A Telegram Torrent (and youtube-dl) Leecher based on [Pyrogram](https://github.com/pyrogram/pyrogram).

## Working Leecher Group:
#### This is my [Group](http://t.me/discovery_mirror). You can test my bot and leech something.
<a href="https://t.me/discovery_mirror"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>

# Features:
1. Google Drive link cloning using gclone.(wip)
2. Telegram File mirrorring to cloud along with its unzipping, unrar and untar
3. Drive/Teamdrive support/All other cloud services rclone.org supports
4. Unzip
5. Unrar
6. Untar
7. Custom file name
8. Custom commands
9. Get total size of your working cloud directory
10. You can also upload files downloaded from /ytdl command to gdrive using `/ytdl gdrive` command.
11. You can also deploy this on your VPS
12. Option to select either video will be uploaded as document or streamable
13. Added /renewme command to clear the downloads which are not deleted automatically.
14. Added support for youtube playlist
    
# TO-DO
-   ~Gdrive file clonning using Gclone~ `DONE ✓`
-   [ ] Adding mp3 files support while playlist downloading.
-   [ ] Password support while Unarchiving the files.
-   [ ] Selection of required files during leeching the big files using aria(/leech command)

### Credit goes to SpEcHiDe for his Publicleech repo.

## Installation:
For any kind of help feel free to ask in my [Telegram Group](http://t.me/linux_repo) [Linux Repositories](http://t.me/linux_repo).
- <a href="https://t.me/linux_repo"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>

#### The Easy Way!
Must [Fork](https://github.com/AbirHasan2005/Telegram-Leech-Bot/fork) this repo before deploying. And don't upload with your name without proper credit. For any kind of help must ask in my [Telegram Group](http://t.me/linux_repo). <a href="https://t.me/linux_repo"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>


#No-Deploy Need Deploy [Fork This Repo](https://github.com/AbirHasan2005/Telegram-Leech-Bot)


- Recently there is a problem with Heroku deployment. So try with a **Better Luck**. If need any help than must ask in my [Telegram Group](http://t.me/linux_repo).

- Better to buy a Linux VPS like: Ubuntu or Kali Linux. Then deploy on it. If need any help then ask in my [Telegram Group](http://t.me/linux_repo) or in [GBotStore](https://t.me/joinchat/ICUArRi8B6VNedA20RS-sw).

### The Legacy Way of Deployment:
Simply clone the repository and run the main file:

```bash
git clone https://github.com/AbirHasan2005/Telegram-Leech-Bot telegram-leech-bot
cd telegram-leech-bot
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py appropriately>
python3 -m tobrot
```

### Here is an example of config.py:
```python
from tobrot.sample_config import Config

class Config(Config):
  TG_BOT_TOKEN = ""
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  AUTH_CHANNEL = [-1001234567890]
```

### Variable Explanations

##### Mandatory Variables

* `TG_BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.

* `APP_ID`: Get this values from [my.telegram.org/apps](https://my.telegram.org/apps).
* `API_HASH`: Get this values from [my.telegram.org/apps](https://my.telegram.org/apps).
  * N.B.: if Telegram is blocked by your ISP, try our [Telegram bot](https://telegram.dog/UseTGXBot) to get the IDs.

* `AUTH_CHANNEL`: Create a Super Group in Telegram, add [@MissRose_bot](http://t.me/MissRose_bot) to the group, and send `/id` in the chat, to get this value.

* `RCLONE_CONFIG`: Create the rclone config using the rclone.org and read the rclone section for the next.

* `DESTINATION_FOLDER`: Name of your folder in ur respective drive where you want to upload the files using the bot.

* `OWNER_ID`: ID of the bot owner, He/she can be abled to access bot in bot only mode too(private mode).

##### Set Rclone

1. Set Rclone locally by following the official repo : https://rclone.org/docs/
2. Get your `rclone.conf` file. That will look like this:
```
[NAME]
type = 
scope =
token =
client_id = 
client_secret = 

```
3. Only copy the config of drive u want to upload file.
4. Copy the entries of `rclone.conf` 
5. Your copied config should look like this:
 ```
type = 
scope =
token =
client_id = 
client_secret = 

and everythin except `[NAME]`

```

6. Paste copied config in `RCLONE_CONFIG`

7. Hit deploy button.
8. Examples:-
<p align="center">

  <img src="https://raw.githubusercontent.com/gautamajay52/TorrentLeech-Gdrive/master/rclone.jpg" width="470" height="150">

</p>

## FAQ

##### Optional Configuration Variables

* `DOWNLOAD_LOCATION`

* `MAX_FILE_SIZE`

* `TG_MAX_FILE_SIZE`

* `FREE_USER_MAX_FILE_SIZE`

* `MAX_TG_SPLIT_FILE_SIZE`

* `CHUNK_SIZE`

* `MAX_MESSAGE_LENGTH`

* `PROCESS_MAX_TIMEOUT`

* `ARIA_TWO_STARTED_PORT`

* `EDIT_SLEEP_TIME_OUT`

* `MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START`

* `FINISHED_PROGRESS_STR`

* `UN_FINISHED_PROGRESS_STR`

* `TG_OFFENSIVE_API`

* `CUSTOM_FILE_NAME`

* `LEECH_COMMAND`

* `YTDL_COMMAND`

* `GLEECH_COMMAND`

* `TELEGRAM_LEECH_COMMAND_G`

* `PYTDL_COMMAND_G`

* `CLONE_COMMAND_G`

* `UPLOAD_AS_DOC`: Takes two option True or False. If True file will be uploaded as document. This is for people who wants video files as document instead of streamable.

* `INDEX_LINK`: (Without `/` at last of the link, otherwise u will get error) During creating index, plz fill `Default Root ID` with the id of your `DESTINATION_FOLDER` after creating. Otherwise index will not work properly.
## Available Commands

* `/gclone`: This command is used to clone gdrive files or folder using gclone.
       
       Syntax:- `[ID of the file or folder][one space][name of your folder only(If the id is of file, don't put anything)]` and then reply /gclone to it.
       
* `/log`: This will send you a txt file of the logs.

* `/ytdl`: This command should be used as reply to a [supported link](https://ytdl-org.github.io/youtube-dl/supportedsites.html)

* `/pytdl`: This command will download videos from youtube playlist link and will upload to telegram.

* `/ytdl gdrive`: This will download and upload to your cloud.

* `/pytdl gdrive`: This download youtube playlist and upload to your cloud.

* `/leech`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [this command will SPAM the chat and send the downloads a seperate files, if there is more than one file, in the specified torrent]

* `/leech archive`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [This command will create a .tar.gz file of the output directory, and send the files in the chat, splited into PARTS of 1024MiB each, due to Telegram limitations]

* `/gleech`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. And this will download the files from the given link or torrent and will upload to the cloud using rclone.

* `/gleech archive` This command will compress the folder/file and will upload to your cloud.

* `/leech unzip`: This will unzip the .zip file and dupload to telegram.

* `/gleech unzip`: This will unzip the .zip file and upload to cloud.

* `/leech unrar`: This will unrar the .rar file and dupload to telegram.

* `/gleech unrar`: This will unrar the .rar file and upload to cloud.

* `/leech untar`: This will untar the .tar file and upload to telegram.

* `/gleech untar`: This will untar the .tar file and upload to cloud..

* `/tleech`: This will mirror the telegram files to ur respective cloud cloud.

* `/tleech unzip`: This will unzip the .zip telegram file and upload to cloud.

* `/tleech unrar`: This will unrar the .rar telegram file and upload to cloud.

* `/tleech untar`: This will untar the .tar telegram file and upload to cloud.

* `/getsize`: This will give you total size of your destination folder in cloud.

* `/renewme`: This will clear the remains of downloads which are not getting deleted after upload of the file or after /cancel command. 


* [Only work with direct link and youtube link for now]It is like u can add custom name as prefix of the original file name.
Like if your file name is `gk.txt` uploaded will be what u add in `CUSTOM_FILE_NAME` + `gk.txt`

Only works with direct link/youtube link.No magnet or torrent.

And also added custom name like...

You have to pass link as 
`www.download.me/gk.txt | new.txt`

the file will be uploaded as `new.txt`.

## Process to run this BOT on Linux VPS:

- Clone this repo:
```
git clone https://github.com/AbirHasan2005/Telegram-Leech-Bot telegram-leech-bot
cd telegram-leech-bot
```

- Install requirements
For Debian based distros
```
sudo apt install python3

sudo snap install docker
```
Install Docker by following the [official docker docs](https://docs.docker.com/engine/install/debian/).

## Setting up config file
```
cp tobrot/g_config.py tobrot/config.py
```
Follow and fill all the required variables that were already filled in the sample config file, but with your details. And you can also fill all other variables according to your need and all those are explained above already.

## Deploying

- Start docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
sudo docker build . -t torrentleech-gdrive
```
- Run the image:
```
sudo docker run torrentleech-gdrive
```


## How to Use?

* send any one of the available command, as a reply to a valid link/magnet/torrent.


## Credits, and Thanks to
* [GautamKumar](https://github.com/gautamajay52/TorrentLeech-Gdrive) for adding some cool features.
* [SpEcHiDe](https://github.com/SpEcHiDe/PublicLeech) for his wonderful code.
* [Rclone Team](https://rclone.org) for theirs awesome tool.
* [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram).
* [Robots](https://telegram.dog/Robots) for their [@UploadBot](https://telegram.dog/UploadBot).
* [@AjeeshNair](https://telegram.dog/AjeeshNait) for his [torrent.ajee.sh](https://torrent.ajee.sh).
* [@gotstc](https://telegram.dog/gotstc), @aryanvikash, [@HasibulKabir](https://telegram.dog/HasibulKabir) for their TORRENT groups.
* [![CopyLeft](https://telegra.ph/file/b514ed14d994557a724cb.jpg)](https://telegra.ph/file/fab1017e21c42a5c1e613.mp4 "CopyLeft Credit Video").

* Can't give a [Thanks](http://t.me/linux_repo) to [me](https://github.com/AbirHasan2005). :|
