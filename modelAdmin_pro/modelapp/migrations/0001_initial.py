# Generated by Django 3.2 on 2022-08-29 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_no', models.IntegerField(default=False)),
                ('Name', models.CharField(blank=True, max_length=255)),
                ('Email', models.EmailField(blank=True, max_length=255)),
                ('division', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]