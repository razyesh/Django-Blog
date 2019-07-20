# Generated by Django 2.2.3 on 2019-07-20 03:18

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20190718_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('video', ckeditor_uploader.fields.RichTextUploadingField()),
                ('thumbnail', models.ImageField(default='home/images/default.png', upload_to='video/images')),
                ('publish', models.BooleanField(default=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]