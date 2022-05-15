# Generated by Django 2.1.5 on 2019-02-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auction_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='desc',
            field=models.CharField(blank=True, default='No description provided.', max_length=2000),
        ),
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(blank=True, default='auction_images/default/default.svg', upload_to='auction_images/'),
        ),
    ]
