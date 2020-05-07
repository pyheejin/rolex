# Generated by Django 3.0.5 on 2020-05-07 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category'),
        ),
        migrations.AlterModelTable(
            name='feature',
            table='features',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]