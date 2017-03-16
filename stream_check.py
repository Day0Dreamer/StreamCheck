import requests
import logging
import winsound
import os.path
from time import sleep, asctime

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

default_sound = 'default.wav'

try:
    cfg = open('streamers.cfg')
    logging.info('streamers.cfg loaded')
    cfg = cfg.readlines()
except FileNotFoundError:
    logging.critical('ERROR! streamers.cfg is not found.')

while 1:
    for streamers in cfg:
        streamers = streamers.strip()
        gg_response = requests.get('https://goodgame.ru/api/getchannelstatus?fmt=json&id='+streamers)
        gg_response = gg_response.json()

        if not gg_response:
            logging.error("Wrong streamer's key ("+streamers+")")

        for i in gg_response:
            sound_notification = default_sound
            online_sound_wav = gg_response[i]['key']+'.wav'
            print(asctime(),'|', gg_response[i]['status'],'|', gg_response[i]['url'])

            if gg_response[i]['status'] != "Dead":
                if os.path.exists(online_sound_wav):
                    sound_notification = gg_response[i]['key']+'.wav'
                    logging.info(sound_notification+' sound exists')
                else:
                    logging.error('sound for '+gg_response[i]['key']+' does not exist')

                winsound.PlaySound(sound_notification, winsound.SND_FILENAME)
    sleep(60)

