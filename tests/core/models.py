# A couple models for Haystack to test with.
import datetime
from django.db import models


class MockTag(models.Model):
    name = models.CharField(max_length=32)


class MockModel(models.Model):
    author = models.CharField(max_length=255)
    foo = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    tag = models.ForeignKey(MockTag)
    score = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.author
    
    def hello(self):
        return 'World!'


class AnotherMockModel(models.Model):
    author = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.author


class AThirdMockModel(AnotherMockModel):
    average_delay = models.FloatField(default=0.0)
    view_count = models.PositiveIntegerField(default=0)


class CharPKMockModel(models.Model):
    key = models.CharField(primary_key=True, max_length=10)


class AFourthMockModel(models.Model):
    author = models.CharField(max_length=255)
    editor = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.author

class SoftDeleteManager(models.Manager):
    def get_query_set(self):
        return super(SoftDeleteManager, self).get_query_set().filter(deleted=False)

    def complete_set(self):
        return super(SoftDeleteManager, self).get_query_set()

class AFifthMockModel(models.Model):
    author = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __unicode__(self):
        return self.author

class ASixthMockModel(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()

    def __unicode__(self):
        return self.name
