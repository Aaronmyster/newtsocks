from models import *
from lxml import html
import requests
import datetime
import sys

def main():
	companies = Company.select()
	ns = NewsSource.select().where(NewsSource.name=='Reuters').get()

	for c in companies:
		firstURL = 'http://www.reuters.com/search?blob="'+c.name.replace(' ','+')+'"'
		readSearchPage(c,ns,firstURL,1)

	print 'DONE!'

def readSearchPage(companyModel,newsSourceModel,url,page):
	if page == 5:
		return
	
	print 'Reading Page: {0}'.format(page)

	tree = html.fromstring(requests.get(url).text)

	#Get the list of all article URL's
	articleURLs = tree.xpath("//*[@class='searchHeadline']/a/@href")

	#add every article on the search page to the database
	for articleUrl in articleURLs:
		addNewsArticle(companyModel,newsSourceModel,articleUrl)

	#go to the next page, and do the same thing...
	nextURL = tree.xpath("//*[@class='next']/a/@href")[0]
	readSearchPage(companyModel,newsSourceModel,nextURL,page+1)

def addNewsArticle(companyModel,newsSourceModel,url):
	tree = html.fromstring(requests.get(url).text)
	
	#Need the article title
	title = tree.xpath('//h1/text()')[0]

	#Need the text of the article
	textElements = tree.xpath("//*[@id='articleText']//*/text()")
	text = ""
	for t in textElements:
		text += t

	#TODO: Need the date field
	dateText = tree.xpath("//div[@id='articleInfo']//span[@class='timestamp']/text()")[0]
	print dateText
	
	date = datetime.datetime.strptime(dateText, "%a %b %d, %Y %I:%M%p %Z").date()
	print dateText

	News.create(company=companyModel,
		newsSource=newsSourceModel,
		title=title,
		text=text,
		url=url,
		date = date
	)
	print "Added: "+title

if __name__ == '__main__':
    sys.exit(main())