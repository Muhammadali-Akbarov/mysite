# Generated by Django 4.0 on 2022-07-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcategory',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
