#python imports
from datetime import datetime

#django imports
from django.conf import settings
from django.utils.text import slugify

#inter app imports

#third party imports
from mongoengine import *

class Article(Document):
    title = StringField(max_length=200,db_field='ti')
    keywords = StringField(db_field='kw')
    publish_date = DateTimeField(db_field='pd')
    created_date = DateTimeField(db_field='cd',default=datetime.now)
    modified_date = DateTimeField(db_field='md')
    short_description = StringField(db_field='sd')
    author = StringField(max_length=200,db_field='au')
    source = StringField(max_length=100,db_field='so')
    title_slug = StringField(db_field='ts')
    published = BooleanField(db_field='pu')
    image = StringField(db_field='im')
    landing_url = StringField(db_field='lu')

    def __str__(self):
        return "{} | {}".format(self.title,self.id)

    def save(self,**kwargs):
        created = not bool(getattr(self,"id"))
        self.modified_date = datetime.now()
        original_object = None
        
        if not created:
            original_object = Article.objects.get(id=self.id)

        if created or original_object.title!=self.title:
            self.title_slug = str(slugify(self.title))
        return super(Article, self).save(**kwargs)

    meta = {
        'collection': 'Article',
        'indexes': [
          'keywords',
          'publish_date'
        ]
    }
