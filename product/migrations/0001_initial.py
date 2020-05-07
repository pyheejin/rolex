# Generated by Django 3.0.5 on 2020-05-07 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bezel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField(max_length=1000)),
            ],
            options={
                'db_table': 'bezels',
            },
        ),
        migrations.CreateModel(
            name='Bracelet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField(max_length=1000)),
            ],
            options={
                'db_table': 'bracelets',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'collections',
            },
        ),
        migrations.CreateModel(
            name='Dial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField(max_length=1000)),
            ],
            options={
                'db_table': 'dials',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField(max_length=1000)),
                ('background_image', models.URLField(max_length=1000)),
            ],
            options={
                'db_table': 'materials',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail', models.URLField(max_length=1000)),
                ('header_image', models.URLField(max_length=1000)),
                ('header_background_image', models.URLField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('sub_description', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('middle_image', models.URLField(max_length=1000)),
                ('middle_thumbnail_image', models.URLField(max_length=1000)),
                ('middle_title', models.CharField(max_length=50)),
                ('middle_sub_title', models.CharField(max_length=50)),
                ('middle_description', models.CharField(max_length=1000)),
                ('bezel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Bezel')),
                ('bracelet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Bracelet')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Collection')),
                ('dial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Dial')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Material')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Size')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=50)),
                ('thumbnail_image', models.URLField(max_length=1000)),
                ('image', models.URLField(max_length=1000)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product')),
            ],
        ),
        migrations.AddField(
            model_name='dial',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Material'),
        ),
        migrations.AddField(
            model_name='bracelet',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Material'),
        ),
        migrations.AddField(
            model_name='bezel',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Material'),
        ),
    ]