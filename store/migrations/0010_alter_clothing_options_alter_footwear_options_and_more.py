# Generated by Django 5.0.6 on 2024-06-09 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_otherproduct_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clothing',
            options={'verbose_name': 'DRABUŽIAI', 'verbose_name_plural': 'DRABUŽIAI'},
        ),
        migrations.AlterModelOptions(
            name='footwear',
            options={'verbose_name': 'AVALYNĖ', 'verbose_name_plural': 'AVALYNĖ'},
        ),
        migrations.AlterModelOptions(
            name='otherproduct',
            options={'verbose_name': 'KITOS PREKĖS', 'verbose_name_plural': 'KITOS PREKĖS'},
        ),
    ]