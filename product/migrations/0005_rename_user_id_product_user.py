# Generated by Django 5.0.4 on 2024-05-06 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_id',
            new_name='user',
        ),
    ]
