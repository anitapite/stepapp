# Generated by Django 3.1.7 on 2021-05-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0002_auto_20210403_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='notes',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]