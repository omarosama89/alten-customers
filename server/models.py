from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from .remote_customer_api import RemoteCustomerApi


@python_2_unicode_compatible
class Customer(models.Model):
    __original_first_name = None
    __original_last_name = None

    def __init__(self, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.__original_first_name = self.first_name
        self.__original_last_name = self.last_name

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    remote_id = models.IntegerField(blank=True, null=True)

    def first_name_changed(self):
        return self.first_name != self.__original_first_name

    def last_name_changed(self):
        return self.last_name != self.__original_last_name


@receiver(post_save, sender=Customer)
def callback(sender, instance, **kwargs):
    if kwargs['created']:
        RemoteCustomerApi.create(instance)
    elif instance.first_name_changed() or instance.last_name_changed():
        RemoteCustomerApi.update(instance)
