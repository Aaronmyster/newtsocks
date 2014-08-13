from datetime import datetime
from models import News
from models import OpinionAPI
from models import OpinionAPIResponse
import unirest
import sys

#This is a script that will call out to a Mashape API to get the sentament of the 
#articles. 

def main():

	#Only 1 API at a time for now
	api = OpinionAPI.select().where(OpinionAPI.name == "Text-Processing").get()

	#Get the list of articles
	news = News.select()

	#Go through each news article, and add Sentament
	for n in news:
		addResponse(api,n)

def addResponse(api,news):
	try:
		#Send the article text to the text processing API
		# These code snippets use an open-source library. http://unirest.io/python
		response = unirest.post(api.url,
		  headers={"X-Mashape-Key": api.key, "Content-Type": "application/x-www-form-urlencoded"},
		  params={"language": "english", "text": news.text}
		)

		#Need the date I made this request
		d = datetime.now()	

		#Need the score
		score = getScore(response)

		#Add the response to the db
		OpinionAPIResponse.create(api=api,news=news,date=d,response=response.body,score=score)

		print "Added Response for {0}".format(news.url)
	except Exception, e:
		print "Error adding Response for {0}".format(news.url)
	
	
def getScore(responseText):
	try:
		neg = float(re.search("'neg': (([0-9]|\.)*)",responseText).group(1))
		pos = float(re.search("'pos': (([0-9]|\.)*)",responseText).group(1))
		score = pos - neg
		return score
	except Exception, e:
		return 0


if __name__ == '__main__':
	sys.exit(main())

