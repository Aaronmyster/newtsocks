from models import *
from lxml import html
import requests

def addNewsArticle(companyModel,newsSourceModel,htmlString,url):
	tree = html.fromstring(htmlString)
	#Need the article title
	title = tree.xpath('//h1/text()')[0]

	#Need the text of the article
	textElements = tree.xpath("//*[@id='articleText']//*/text()")
	text = ""
	for t in textElements:
		text += t

	News.create(company=companyModel,
		newsSource=newsSourceModel,
		title=title,
		text=text,
		url=url
	)
	print "Added: "+title

def readSearchPage(companyModel,newsSourceModel,url):
	#page = requests.get('http://www.reuters.com/search?blob="'+c.name.replace(' ','+')+'"')
	#tree = html.fromstring(page.text)
	tree = html.fromstring(file("/home/aaron/Downloads/sr.html").read())
	articleURLs = tree.xpath("//*[@class='searchHeadline']/a/@href")

	#add every article on the search page to the database
	#for url in articleURLs:
		#htmlString = requests.get(url).text
		#addNewsArticle(companyModel,newsSourceModel)

	#go to the next page, and do the same thing...
	nextUrl = tree.xpath("//*[@class='next']/a/@href")[0]
	print nextUrl

def main():
	#Just testing a single company for now
	company = Company.select().where(Company.id==2).get()
	newsSource = NewsSource.select().where(NewsSource.name=='Reuters').get()

	readSearchPage(company,newsSource,"")

main()
#print articleURLs
#addNewsArticle(c,newsSource,file("/home/aaron/Downloads/article.html").read(),"bla")