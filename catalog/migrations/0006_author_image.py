# Generated by Django 2.2.5 on 2019-09-20 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20190919_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', null=True, upload_to='images', verbose_name='Ссылка картинки'),
        ),
    ]