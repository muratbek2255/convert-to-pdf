from django.db import models


class Customer(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    logo = models.ImageField(verbose_name='Image')
    description = models.TextField(verbose_name='Description')
    updated_at = models.DateTimeField(verbose_name='Update time', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Create time', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
