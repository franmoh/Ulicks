# Generated by Django 4.1.6 on 2023-04-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
