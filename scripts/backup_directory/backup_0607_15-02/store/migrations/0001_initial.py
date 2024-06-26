# Generated by Django 5.0.6 on 2024-06-06 13:22

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Pavadinimas')),
            ],
            options={
                'verbose_name': 'Kategorija',
                'verbose_name_plural': 'Kategorijos',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Pavadinimas')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Kategorija')),
            ],
            options={
                'verbose_name': 'Subkategorija',
                'verbose_name_plural': 'Subkategorijos',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10, verbose_name='Dydis')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcategory', verbose_name='Subkategorija')),
            ],
            options={
                'verbose_name': 'Dydis',
                'verbose_name_plural': 'Dydžiai',
                'ordering': ['size'],
            },
        ),
        migrations.CreateModel(
            name='OtherProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('genre', models.CharField(choices=[('baby', 'Kūdikiams'), ('girls', 'Mergaitėms'), ('boys', 'Berniukams'), ('unisex', 'Unisex')], max_length=10, verbose_name='Lytis')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Prekės ženklas')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='Aprašymas')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Kaina')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Kiekis sandėlyje')),
                ('is_on_sale', models.BooleanField(default=False, verbose_name='Pažymėti, jei prekė yra išpardavime')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Nuotrauka')),
                ('sizes', models.ManyToManyField(blank=True, to='store.size', verbose_name='Dydžiai')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcategory', verbose_name='Kategorijos tipas')),
            ],
            options={
                'verbose_name': 'Kitos prekės',
                'verbose_name_plural': 'Kitos prekės',
            },
        ),
        migrations.CreateModel(
            name='Footwear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('genre', models.CharField(choices=[('baby', 'Kūdikiams'), ('girls', 'Mergaitėms'), ('boys', 'Berniukams'), ('unisex', 'Unisex')], max_length=10, verbose_name='Lytis')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Prekės ženklas')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='Aprašymas')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Kaina')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Kiekis sandėlyje')),
                ('is_on_sale', models.BooleanField(default=False, verbose_name='Pažymėti, jei prekė yra išpardavime')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Nuotrauka')),
                ('sizes', models.ManyToManyField(blank=True, to='store.size', verbose_name='Dydžiai')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcategory', verbose_name='Kategorijos tipas')),
            ],
            options={
                'verbose_name': 'Avalynė',
                'verbose_name_plural': 'Avalynė',
            },
        ),
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('genre', models.CharField(choices=[('baby', 'Kūdikiams'), ('girls', 'Mergaitėms'), ('boys', 'Berniukams'), ('unisex', 'Unisex')], max_length=10, verbose_name='Lytis')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Prekės ženklas')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='Aprašymas')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Kaina')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Kiekis sandėlyje')),
                ('is_on_sale', models.BooleanField(default=False, verbose_name='Pažymėti, jei prekė yra išpardavime')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Nuotrauka')),
                ('sizes', models.ManyToManyField(blank=True, to='store.size', verbose_name='Dydžiai')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcategory', verbose_name='Kategorijos tipas')),
            ],
            options={
                'verbose_name': 'Drabužis',
                'verbose_name_plural': 'Drabužiai',
            },
        ),
    ]
