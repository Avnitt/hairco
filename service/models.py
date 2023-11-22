from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to='service', null=True)

    def __str__(self):
        return self.title

class Subservice(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.ImageField(upload_to='subservice', null=True)
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                related_name='subservices')

    def __str__(self):
        return self.title

class Addon(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.ImageField(upload_to='addon', null=True)

    def __str__(self):
        return self.title
