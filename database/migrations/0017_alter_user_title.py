# Generated by Django 4.1.3 on 2023-02-17 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_user_signup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.title'),
        ),
    ]
