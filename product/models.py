from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class Collection(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)

	class Meta:
		db_table = 'collections'

class Size(models.Model):
	size = models.IntegerField()

	class Meta:
		db_table = 'sizes'

class Material(models.Model):
	name = models.CharField(max_length=50)
	image = models.URLField(max_length=1000)
	background_image = models.URLField(max_length=1000)

	class Meta:
		db_table = 'materials'

class Bezel(models.Model):
	material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	image = models.URLField(max_length=1000)

	class Meta:
		db_table = 'bezels'

class Bracelet(models.Model):
	material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	image = models.URLField(max_length=1000)

	class Meta:
		db_table = 'bracelets'

class Dial(models.Model):
	material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	image = models.URLField(max_length=1000)

	class Meta:
		db_table = 'dials'

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)
	size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
	material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
	bezel = models.ForeignKey(Bezel, on_delete=models.SET_NULL, null=True)
	bracelet = models.ForeignKey('Bracelet', on_delete=models.SET_NULL, null=True)
	dial = models.ForeignKey(Dial, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	thumbnail = models.URLField(max_length=1000)
	header_image = models.URLField(max_length=1000)
	header_background_image = models.URLField(max_length=1000)
	description = models.CharField(max_length=1000)
	sub_description = models.CharField(max_length=1000)
	price = models.IntegerField()
	middle_image = models.URLField(max_length=1000)
	middle_thumbnail_image = models.URLField(max_length=1000)
	middle_title = models.CharField(max_length=50)
	middle_sub_title = models.CharField(max_length=50)
	middle_description = models.CharField(max_length=1000)

	class Meta:
		db_table = 'products'

class Feature(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=50)
	sub_title = models.CharField(max_length=50)
	thumbnail_image = models.URLField(max_length=1000)
	image = models.URLField(max_length=1000)
	description = models.CharField(max_length=1000)

	class Meta:
		db_table = 'features'
