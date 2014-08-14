from lxml import html
from models import Company
from models import News
from models import NewsSource
import datetime
import requests
import sys

baseURL = 'http://www.reuters.com'

def main():

    #Select companies that don't have any articles
    companies = Company.raw(
        """
        Select * 
        FROM company 
        WHERE id not in (
            SELECT company_id 
            from news
        )
        """
    )



    ns = NewsSource.select().where(NewsSource.name=='Reuters').get()

    for c in companies:
        print "Finding stories about "+c.name
        firstURL = baseURL+'/search?blob="'+c.name.replace(' ','+')+'"'
        readSearchPage(c,ns,firstURL,1)

    print 'DONE!'

def readSearchPage(companyModel,newsSourceModel,url,page):
    try:
        print 'Reading Page: {0}'.format(page)

        tree = html.fromstring(requests.get(url).text)

        # Get the list of all article URL's
        articleURLs = tree.xpath("//*[@class='searchHeadline']/a/@href")

        # add every article on the search page to the database
        for articleUrl in articleURLs:
            addNewsArticle(companyModel,newsSourceModel,articleUrl)

        # go to the next page, and do the same thing...
        nextURL = tree.xpath("//*[@class='next']/a/@href")[0]
        readSearchPage(companyModel,newsSourceModel,baseURL+nextURL,page+1)

    except Exception, e:
        print e
        print "There was an error on page {0}. Moving on.".format(page)

def addNewsArticle(companyModel,newsSourceModel,url):
    tree = html.fromstring(requests.get(url).text)
    
    # Need the article title
    title = tree.xpath('//h1/text()')[0]

    # Need the text of the article
    textElements = tree.xpath("//*[@id='articleText']//*/text()")
    text = ""
    for t in textElements:
        text += t

    # Need the date field
    dateText = tree.xpath("//div[@id='articleInfo']//span[@class='timestamp']/text()")[0]
    date = datetime.datetime.strptime(dateText[:-4], "%a %b %d, %Y %I:%M%p").date()

    News.create(
        company=companyModel,
        newsSource=newsSourceModel,
        title=title,
        text=text,
        url=url,
        date = date
    )
    print "Added: "+title

if __name__ == '__main__':
    sys.exit(main())