import threading
from feeds import feed_reddit  

def startFeeds():
	# Start feed modules
	feed_reddit.start()

	#Call startFeeds every x seconds
	threading.Timer(1200, startFeeds).start();

startFeeds()