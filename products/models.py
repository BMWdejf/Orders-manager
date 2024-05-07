from django.db import models


# Model for Category
class Category(models.Model):
    cat_title = models.CharField(max_length=150, unique=True)
    cat_description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.cat_title

# Model for VAT
class Vat(models.Model):
    vat_title = models.CharField(max_length=150, unique=True)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    class Meta:
        verbose_name_plural = 'Vat'

    def __str__(self):
        return self.vat_title

# Model for Products
class Product(models.Model):
    active = models.BooleanField(default=False)
    pro_title = models.CharField(max_length=150, unique=True)
    pro_description = models.TextField(blank=True)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    vat = models.ForeignKey(Vat, null=True, on_delete=models.CASCADE)
    code_plu = models.CharField(max_length=150, unique=False)
    ean_code = models.PositiveSmallIntegerField(null=False)
    qanty = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products', null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.pro_title

class Unit(models.Model):
    unit_title = models.CharField(max_length=150, unique=True)
    char = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name_plural = 'Units'

    def __str__(self):
        return self.unit_title