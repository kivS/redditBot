'''
	 pushbullet & push notifications
'''
import requests,logging,json

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

with open('configs/config.json', 'r+') as f:
	config = json.loads(f.read())

ACCESS_TOKEN = config.get('pushbullet_access_token')
PUSH_LINK = config.get('pushbullet_push_link')

def push_link_toChannel(channel_tag,title,body,url):
	headers = {
		'Access-Token': ACCESS_TOKEN,
		'Content-Type':'application/json'
	}
	logging.debug(headers)
	data={
		'channel_tag': channel_tag,
  		'type':  'link', 
  		'title': title, 
        'body':  body ,
        'url':   url,
        'direction':'self',
        'dismissed':False
	}
	logging.debug(data)
	r = requests.post(PUSH_LINK,data=json.dumps(data),headers=headers)
	logging.debug(r.text)

#push_link_toChannel("feederbot","test n:5","text of test n5","https://www.reddit.com/r/forhire/new.json")