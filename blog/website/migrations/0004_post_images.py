# Generated by Django 5.1.1 on 2024-10-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
