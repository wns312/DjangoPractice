from django.db import models


class Base:
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("After save : ", self)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        print("After delete : ", self)


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)

    class Meta:
        abstract = True


class CreatedUpdatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
