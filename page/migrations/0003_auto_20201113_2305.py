# Generated by Django 3.1.1 on 2020-11-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='page'),
        ),
    ]
