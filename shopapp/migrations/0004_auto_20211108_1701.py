# Generated by Django 2.2.12 on 2021-11-08 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0003_auto_20211108_1024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categoties'},
        ),
    ]
