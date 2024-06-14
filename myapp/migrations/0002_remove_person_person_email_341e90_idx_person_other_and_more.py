# Generated by Django 4.2.7 on 2024-06-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='person',
            name='person_email_341e90_idx',
        ),
        migrations.AddField(
            model_name='person',
            name='other',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['email', 'uid'], name='person_email_39d62a_idx'),
        ),
    ]
