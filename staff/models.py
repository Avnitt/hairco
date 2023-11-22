from django.db import models
from customauth.models import User
from service.models import Subservice

class Professional(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    image_url = models.ImageField(upload_to='professional', null=True)
    subservices = models.ManyToManyField(Subservice,
                                         related_name='professionals')

    def save(self, *args, **kwargs):
        self.user.is_staff = True
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.phone

class Slot(models.Model):
    start_time = models.DateTimeField()
    professional = models.ForeignKey(Professional,
                                     on_delete=models.CASCADE,
                                     related_name='slots')

    def __str__(self):
        return self.start_time.strftime("%m %d %H:%M")
