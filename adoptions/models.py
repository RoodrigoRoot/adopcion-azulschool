from django.db import models
from django.conf import settings
# Create your models here.

class Adoption(models.Model):
                            
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User", on_delete=models.CASCADE)
    pet = models.ForeignKey("pets.Pet", verbose_name="Pet", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date",  auto_now_add=True)
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return "{}-{}".format(self.pet, self.user)