# Generated by Django 3.2.7 on 2021-10-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=150)),
                ('author', models.TextField(max_length=150)),
                ('description', models.TextField(default='No description', max_length=150)),
                ('price', models.TextField(max_length=150)),
                ('rating', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
    ]
