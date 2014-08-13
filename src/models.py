from peewee import CharField
from peewee import DateTimeField
from peewee import DoubleField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import Model
from peewee import SqliteDatabase

db = SqliteDatabase('../newtsocks.db')

class BaseModel(Model):
    class Meta(object):
        database = db

class Company(BaseModel):
    name = CharField()
    ticker = CharField()

class NewsSource(BaseModel):
    name = CharField()    
    url = CharField()

class News(BaseModel):
    company = ForeignKeyField(Company, related_name='news.company')
    newsSource = ForeignKeyField(NewsSource, related_name='news.newsSource')
    title = CharField()
    text = CharField()
    url = CharField()
    date = DateTimeField()

class Price(BaseModel):
    company = ForeignKeyField(Company, related_name='price.company')
    date = DateTimeField()
    openPrice = DoubleField()
    highPrice = DoubleField()
    lowPrice = DoubleField()
    closePrice = DoubleField()
    volumePrice = DoubleField()

class OpinionAPI(BaseModel):
	name = CharField()
	url = CharField()
	key = CharField()

class OpinionAPIResponse(BaseModel):
	api = ForeignKeyField(OpinionAPI, related_name='opinionAPIResponse.OpinionAPI')
	news = ForeignKeyField(News, related_name='opinionAPIResponse.news')
	date = DateTimeField()
	response = CharField()
	score = DoubleField()
    
    
