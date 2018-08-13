from django.db import models
import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
# Create your models here.


class Customer(User):
    phone = models.CharField(
        max_length=12,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{0} - {1}'.format(
            self.id,
            self.name
        )


class Task(models.Model):
    user = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True
    )
    end_date = models.DateTimeField(
        blank=True,
        null=True,
        editable=False
    )
    success = models.BooleanField(
        default=False
    )

    def save(self, *args, **kwargs):
        if not self.id:
            now = datetime.datetime.now()
            self.end_date = now.date() + relativedelta(days=3)
        super().save(*args, **kwargs)


