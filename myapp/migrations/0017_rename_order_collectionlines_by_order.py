# Generated by Django 4.2.3 on 2023-07-30 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_collectionlines_truck_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionlines',
            old_name='order',
            new_name='by_order',
        ),
    ]
