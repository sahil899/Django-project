# Generated by Django 2.2.1 on 2019-11-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0012_auto_20191110_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
