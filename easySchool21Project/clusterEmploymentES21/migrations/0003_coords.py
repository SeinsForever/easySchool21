# Generated by Django 4.2.7 on 2023-11-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusterEmploymentES21', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionName', models.CharField(max_length=10)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
    ]
