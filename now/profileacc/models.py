from django.db import models
from accounts.models import User
# Create your models here.



class DocProfileManager(models.Manager):
    def  create_user(self, address1, birth_date):
        if not address1:
            raise ValueError("Users must have an address")
        prof_obj = self.model(
            address1 = address1,
            birthdate = birthdate,
        )
        prof_obj.save(using=self.db)
        return prof_obj

class DocProfile(models.Model):
    profile = models.OneToOneField(User)
    address1 = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True, blank=True)

    objects = DocProfileManager()

    def __str__(self):
        return self.address1
