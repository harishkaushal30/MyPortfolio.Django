# Generated by Django 3.0.3 on 2020-05-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsection',
            name='error',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]