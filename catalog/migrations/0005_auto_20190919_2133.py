# Generated by Django 2.2.5 on 2019-09-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190915_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', null=True, upload_to='images', verbose_name='Ссылка картинки'),
        ),
    ]
