# Generated by Django 3.0.8 on 2021-03-06 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogposts', '0003_auto_20200717_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, null=True)),
                ('comment_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='blogposts.Post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('-created_at',),
            },
        ),
    ]
