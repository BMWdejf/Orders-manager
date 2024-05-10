from django.db import models

class Contract(models.Model):
    contract_title = models.CharField(max_length=150, unique=True)
    contract_description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    contract_status = models.ForeignKey('ContractStatus', on_delete=models.CASCADE)
    verbose_name_plural = 'Contracts'
    def __str__(self):
        return self.contract_title

class Customer(models.Model):
    customer_name = models.CharField(max_length=150)
    customer_surname = models.CharField(max_length=150)
    customer_address = models.ForeignKey('CustomerAddress', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    verbose_name_plural = 'Customers'
    def __str__(self):
        return self.customer_title


class CustomerAddress(models.Model):
    customer_street = models.CharField(max_length=150)
    customer_home_number = models.PositiveSmallIntegerField()
    customer_city = models.CharField(max_length=150)
    customer_country = models.CharField(max_length=150)
    active = models.BooleanField(default=False)
    verbose_name_plural = 'CustomerAddresses'
    def __str__(self):
        return self.customer_address

class ContractStatus(models.Model):
    status_title = models.CharField(max_length=150, unique=True)
    status_description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    verbose_name_plural = 'ContractStatus'
    def __str__(self):
        return self.status_title