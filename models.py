from peewee import *

db = SqliteDatabase('newtsocks.db')

class Company(Model):
	name = CharField()
	ticker = CharField()

	class Meta:
		database = db


class NewsSource(Model):
	name = CharField()	
	url = CharField()

	class Meta:
		database = db

class News(Model):
	company = ForeignKeyField(Company, related_name='news_fromCompany')
	newsSource = ForeignKeyField(Company, related_name='news_fromSource')
	html = CharField()

	class Meta:
		database = db

class Price(Model):
	company = ForeignKeyField(Company, related_name='prices')
	date = DateTimeField()
	openPrice = DoubleField()
	highPrice = DoubleField()
	lowPrice = DoubleField()
	closePrice = DoubleField()
	volumePrice = DoubleField()

	class Meta:
		database = db

	
	
