# Generated by Django 2.2.3 on 2019-07-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_post_meta_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='meta_content',
            field=models.CharField(max_length=100),
        ),
    ]
