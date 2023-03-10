# Generated by Django 4.1.3 on 2023-01-19 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stain_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tissue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tissue_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='f{Slide.id}.svs', max_length=250)),
                ('stain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.stain')),
                ('tissue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.tissue')),
            ],
        ),
    ]
