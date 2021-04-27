from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    profile_picture = models.ImageField(default="users/me.jpg", upload_to="users/")

    def __str__(self):
        return self.user.username

    # Resize User Profile Picture 
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        profile_picture = Image.open(self.profile_picture.path)
        if profile_picture.height > 300 or profile_picture.width > 300:
            output_size = (300, 300)
            profile_picture.thumbnail(output_size)
        print(profile_picture)
        

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customer_profile.save()
