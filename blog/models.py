from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from  django.db.models import permalink

class Author(models.Model):
    name=models.CharField('שם', max_length=50)
    email = models.EmailField('דואל', unique=True)
    bio = models.TextField('ביוגרפיה')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='מחבר'
        verbose_name_plural='מחברים'

class Post(models.Model):
    # authors = models.ManyToManyField(Author)
    # author = models.ForeignKey('auth.User', blank=True, null=True, default=1)
    author = models.ForeignKey(Author, blank=True, null=True)
    title = models.CharField('כותרת',max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, allow_unicode=True, null=True, blank=True)
    text = RichTextField('טקסט')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField('תאריך פרסום',
        default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='רשומה'
        verbose_name_plural='רשומות'

    # def get_absolute_url(self):
    #     return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    # def get_absolute_url(self):
    #     return reverse("posts:detail", kwargs={"slug": self.slug})