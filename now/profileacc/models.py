from django.db import models
from accounts.models import User
from django.contrib.auth import authenticate, login, get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

User = get_user_model()


#def new_or_get(self, request):
#    user = request.user
#    guest_email_id = request.session.get('guest_email_id')
#    created = False
#    obj = None
#    if user.is_authenticated():
#        'logged in user checkout; remember payment stuff'
#        obj, created = self.model.objects.get_or_create(
#                        user=user, email=user.email)
#    elif guest_email_id is not None:
#        'guest user checkout; auto reloads payment stuff'
#        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
#        obj, created = self.model.objects.get_or_create(
#                                        email=guest_email_obj.email)
#    else:
#        pass
#    return obj, created

class DocProfileManager(models.Manager):
    def  create_user(self, profile, address1, birth_date):
        if not address1:
            raise ValueError("Users must have an address")
        user = self.model(
            address1 = address1,
            birthdate = birthdate,
        )
        return user, profile

class DocProfile(models.Model):
    profile = models.OneToOneField(User, null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True, blank=True)

    objects = DocProfileManager()

    def __str__(self):
        return str(self.address1)

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created: #and instance.email:
        DocProfile.objects.get_or_create(profile=instance,)

post_save.connect(user_created_receiver, sender=User)

#def billing_profile_created_receiver(sender, instance, *args, **kwargs):
#    if not instance.customer_id and instance.email:
#        print("ACTUAL API REQUEST Send to stripe/braintree")
#        customer = stripe.Customer.create(
#                email = instance.email
#            )
#        print(customer)
#        instance.customer_id = customer.id
#post_save.connect(billing_profile_created_receiver, sender=BillingProfile)
