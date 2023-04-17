# Generated by Django 4.0.6 on 2023-04-09 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_item_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image2',
            field=models.ImageField(blank=True, null='True', upload_to='item_image2'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='item',
            name='image3',
            field=models.ImageField(blank=True, null='True', upload_to='item_image3'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.IntegerField(choices=[(0, 'Brand new'), (1, 'Used')], default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.IntegerField(choices=[(0, 'Single (1)'), (1, 'Medium (2-10)'), (2, 'Large (11-100)'), (3, 'Extra-large (101-1000)'), (4, 'Unlimited (>1000)')], default=0),
        ),
    ]
