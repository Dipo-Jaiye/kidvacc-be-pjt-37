# Generated by Django 3.2 on 2021-06-25 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KidVacc', '0002_auto_20210625_0239'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='child_details',
            new_name='child',
        ),
        migrations.RenameModel(
            old_name='user',
            new_name='parent',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='user',
            new_name='parent',
        ),
    ]