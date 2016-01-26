from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name
#
class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_description = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    author = models.ForeignKey('auth.User', blank=True, null=True, default=1)
    title = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, allow_unicode=True, null=True, blank=True)
    #slug = AutoSlugField(populate_from='name', db_index=True,unique=True)
    text = RichTextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)
    # category = models.ForeignKey('Category', blank=True, null=True, default=0)
    # author = models.ForeignKey(Author)
    # categories = models.ManyToManyField(Category)
    # tags = models.ManyToManyField(Tag)

    # def publish(self):
    #     self.published_date = timezone.now()
        # date = timezone.now()
        # self.slug = '%i/%i/%i/%s' % (
        #     date.year, date.month, date.day, slug(self.title)
        # )
        # self.save()
    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    # def save(self):
    #     super(Post, self).save()
    #     date = datetime.date.today()
    #     self.slug = '%i/%i/%i/%s' % (
    #         date.year, date.month, date.day, slugify(self.title)
    #     )
    #     super(Post, self).save()

    # def get_absolute_url(self):
        # return "%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)
        # return ('view_post_detail', None, {'slug':self.slug })

# class Category(models.Model):
#     title = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, db_index=True, unique=True, )
#
#     class Meta:
#         verbose_name_plural = "Categories"
#
#     def __unicode__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return "/categories/%s/" % self.slug
#
# class CategoryToPost(models.Model):
#     post = models.ForeignKey(Post)
#     category = models.ForeignKey(Category)