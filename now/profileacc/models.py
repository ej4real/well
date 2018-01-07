from django.db import models
from accounts.models import User
# Create your models here.



class DocProfileManager(models.Manager):
    def  create_user(self, profile, address1, birth_date):
        if not address1:
            raise ValueError("Users must have an address")
        user = self.model(
            address1 = address1,
            birthdate = birthdate,
        )
        user.save(using=self.db)
        return user, profile

class DocProfile(models.Model):
    profile = models.OneToOneField(User, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True, blank=True)

    objects = DocProfileManager()

    def __str__(self):
        return self.address1
