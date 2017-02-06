
import requests,logging,re,json,time,calendar,sys
from helpers import telegram

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



def start():
	# subreddits wanted
	forhire_url = 'https://www.reddit.com/r/forhire/new/.json'

	forhire_feed_request = requests.get(forhire_url, headers={'User-Agent': 'myFeedbot 0.1 by /u/UserName'})

	# get out if ship starts sinking..
	if forhire_feed_request.status_code != 200: 
		return None
		sys.exit()

	forhire_feed = forhire_feed_request.json()

	# Get feed config file
	with open('configs/reddit_feed_config.json','r+') as f:
		config = json.loads(f.read())
	
	# Go over each post
	for post in forhire_feed['data']['children']:

		# if post was already checked then lets skip it
		if (post['data'].get('created_utc') <= config["lastChecked"]["forHire"]['utc_timestamp']): continue

		# If post has flair 'For Hire' then lets skip it, shall we?!
		if(re.search('for\s*hire', str(post['data'].get('link_flair_text')), re.IGNORECASE) != None): continue

		# Send push notification
		p_title = str(post['data'].get('title'))
		p_url = str(post['data'].get('url'))
		telegram_request = telegram.sendMessage(p_title, p_url)

		logging.debug('Telegram request success: {}'.format(telegram_request.get('ok')))

		if(telegram_request.get('ok') == False):
			logging.error(telegram_request)

		logging.debug('{}-{}'.format(post['data'].get('title'), post['data'].get('created_utc')))

	#save time(now) into config file
	config["lastChecked"]["forHire"]['utc_timestamp'] = calendar.timegm(time.gmtime())
	config["lastChecked"]["forHire"]['human_time'] = time.asctime(time.localtime(config["lastChecked"]["forHire"]['utc_timestamp']))
	
	logging.debug(config['lastChecked']['forHire'])
	
	# Update feed config file
	with open('configs/reddit_feed_config.json','w') as f:
		f.write(json.dumps(config))
