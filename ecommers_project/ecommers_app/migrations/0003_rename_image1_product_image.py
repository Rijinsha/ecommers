# Generated by Django 4.2.7 on 2023-12-02 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommers_app', '0002_rename_image_product_image1_alter_product_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image1',
            new_name='image',
        ),
    ]