from peewee import CharField
from peewee import DateTimeField
from peewee import DoubleField
from peewee import ForeignKeyField
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
    company = ForeignKeyField(Company, related_name='news_fromCompany')
    newsSource = ForeignKeyField(Company, related_name='news_fromSource')
    title = CharField()
    text = CharField()
    url = CharField()
    date = DateTimeField()

class Price(BaseModel):
    company = ForeignKeyField(Company, related_name='prices')
    date = DateTimeField()
    openPrice = DoubleField()
    highPrice = DoubleField()
    lowPrice = DoubleField()
    closePrice = DoubleField()
    volumePrice = DoubleField()

    
    
