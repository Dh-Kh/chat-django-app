# Generated by Django 4.2.1 on 2023-05-25 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_data', '0008_delete_chatnamehistory_delete_messagehistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatNameHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(max_length=200, unique=True)),
                ('chat_creator', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('time_sending', models.DateTimeField(auto_now_add=True)),
                ('chat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat_data.chatnamehistory')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
