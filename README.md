# Newtsocks

It's an anagram for news and stocks.

This is a small project I'm doing to figure out if there's a correlation between public opinion of companies and their stock prices. I'm blogging about it here: [beardedcoder.blogspot.com](http://beardedcoder.blogspot.com/2014/08/data-mining-news-and-stock-market.html)
As of now, it's basically just a web scraper for Reuters, but I'll be adding more soon.

## Status
[![Code Health](https://landscape.io/github/Aaronmyster/newtsocks/master/landscape.png)](https://landscape.io/github/Aaronmyster/newtsocks/master)

## Requirements
* sqlite: apt-get install sqlite3

## Instructions:
1. Clone the repo: git clone https://github.com/Aaronmyster/newtsocks.git
2. cd into the directory: cd newtsocks
3. Install the rest of the requirements: pip install -r reqs.txt
4. cd into the src directory: cd src
5. Run the createDatabase.py script: python createDatabase.py
6. Start Scraping: python reuters.py
... Still working on the rest