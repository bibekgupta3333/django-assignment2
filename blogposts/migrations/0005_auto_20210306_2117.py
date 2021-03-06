# Generated by Django 3.0.8 on 2021-03-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=150, null=True),
        ),
    ]