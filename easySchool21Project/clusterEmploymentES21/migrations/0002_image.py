# Generated by Django 4.2.7 on 2023-11-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusterEmploymentES21', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
