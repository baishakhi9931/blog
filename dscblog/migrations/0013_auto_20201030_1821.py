# Generated by Django 3.1.1 on 2020-10-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscblog', '0012_auto_20201030_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(default='', max_length=20000, verbose_name='Content'),
        ),
    ]
