# Generated by Django 2.2.5 on 2019-09-15 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190915_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]