# Generated by Django 2.2.5 on 2019-09-15 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190915_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='img',
            new_name='image',
        ),
    ]
