from django.db import models
from customauth.models import User
from service.models import Subservice

class Professional(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    image_url = models.ImageField(upload_to='professional', blank=False, null=True)
    subservices = models.ManyToManyField(Subservice,
                                         related_name='professionals')

    def __str__(self):
        return self.user.phone

class Slot(models.Model):
    start_time = models.DateTimeField()
    professional = models.ForeignKey(Professional,
                                     on_delete=models.CASCADE,
                                     related_name='slots')
    booked = models.BooleanField(default=False)

    def __str__(self):
        return self.start_time.strftime("%H:%M")
