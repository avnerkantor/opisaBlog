# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-16 09:34
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='שם')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='דואל')),
                ('bio', models.TextField(null=True, verbose_name='ביוגרפיה')),
            ],
            options={
                'verbose_name': 'מחבר',
                'verbose_name_plural': 'מחברים',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50, verbose_name='category name')),
                ('cat_description', models.CharField(max_length=255, verbose_name='category description')),
            ],
            options={
                'verbose_name': 'קטגוריה',
                'verbose_name_plural': 'קטגוריות',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='כותרת')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=200, null=True, unique=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('summary', models.CharField(blank=True, max_length=400, null=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='תאריך פרסום')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='modified')),
                ('status', models.CharField(choices=[('d', 'טיוטה'), ('a', 'ארכיון'), ('t', 'עמוד'), ('p', 'פרסם')], default='d', max_length=1)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
            options={
                'verbose_name': 'רשומה',
                'verbose_name_plural': 'רשומות',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('tag_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
