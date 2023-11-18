from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Professional, Slot

@receiver(post_save, sender=Professional)
def create_slots_for_professional(sender, instance, **kwargs):
    for day in range(7):
        for hour in range(8, 18):
            start_time = datetime.today() + timedelta(days=day, hours=hour)
            Slot.objects.create(
                professional=instance,
                start_time=start_time,
            )
