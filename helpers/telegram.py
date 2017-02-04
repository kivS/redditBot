import requests, json

with open('configs/config.json', 'r+') as f:
	config = json.loads(f.read())

API_LINK = config.get('telegram_api_link')
TOKEN =    config.get('telegram_api_token')
CHAT_ID =  config.get('telegram_chat_id')


def sendMessage(title, url):
	''' 
		Send reddit post to user

		@ receives: reddit title
		@ receives: reddit url

		@ return: Boolean(result)

	 '''
	#
	#

	bot_link = '{}{}/{}'.format(API_LINK, TOKEN, 'sendMessage')

	headers = {
		'Content-Type':'application/json'
	}

	message = '''
		<b>{}</b>
		{}
	'''.format(title,url)
		
	data={
		'chat_id': CHAT_ID,
		'parse_mode': 'html',
  		'text':  message, 
  
        
	}
		
	return requests.post(bot_link,data=json.dumps(data),headers=headers).json()
