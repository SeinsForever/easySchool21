# Generated by Django 4.2.7 on 2023-11-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusterEmploymentES21', '0006_rename_coordsofhydrogen_hydrogenplaces'),
    ]

    operations = [
        migrations.CreateModel(
            name='carbonPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionName', models.CharField(max_length=10)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
    ]