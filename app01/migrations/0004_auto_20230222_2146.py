# Generated by Django 2.2 on 2023-02-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20230222_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalagreement',
            name='mileageafter',
            field=models.IntegerField(verbose_name='租凭后里程数'),
        ),
        migrations.AlterField(
            model_name='rentalagreement',
            name='mileagebefore',
            field=models.IntegerField(verbose_name='租凭前里程数'),
        ),
    ]
