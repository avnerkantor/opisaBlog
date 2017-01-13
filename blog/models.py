from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User #=> for User who login
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from  django.db.models import permalink
# from managers import PostManger


class Author(models.Model):
    name = models.CharField('שם', max_length=50)
    email = models.EmailField('דואל', unique=True, null=True)
    bio = models.TextField('ביוגרפיה', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'מחבר'
        verbose_name_plural = 'מחברים'


class Category(models.Model):
    cat_name = models.CharField('category name', max_length=50)
    cat_description = models.CharField('category description', max_length=255)

    class Meta:
        verbose_name='קטגוריה'
        verbose_name_plural = 'קטגוריות'

    def __str__(self):
        return self.cat_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    STATUS_CHOICES=(
        ('d', 'טיוטה'),
        ('a', 'ארכיון'),
        ('t', 'עמוד'),
        ('p','פרסם')
    )

    # authors = models.ManyToManyField(Author)
    # author = models.ForeignKey('auth.User', blank=True, null=True, default=1)
    author = models.ForeignKey(Author, blank=True, null=True)
    title = models.CharField('כותרת', max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, allow_unicode=True, null=True, blank=True)
    summary=models.CharField(max_length=400, null=True, blank=True)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField('תאריך פרסום',
                                          default=timezone.now)
    modified = models.DateTimeField('modified', auto_now=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    # objects=PostManger()
    #
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'רשומה'
        verbose_name_plural = 'רשומות'

    # @permalink
    # def get_absolute_url(self):
    #     return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    # def get_absolute_url(self):
    #     return reverse("posts:detail", kwargs={"slug": self.slug})
