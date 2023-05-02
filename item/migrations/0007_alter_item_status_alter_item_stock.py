# Generated by Django 4.0.6 on 2023-05-01 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_alter_item_image_alter_item_image2_alter_item_image3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.IntegerField(choices=[(0, 'Brand new'), (1, 'Used'), (2, 'Other')], default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.IntegerField(choices=[(0, 'Single'), (1, 'Medium'), (2, 'Large'), (3, 'Extra-large'), (4, 'Unlimited')], default=0),
        ),
    ]
