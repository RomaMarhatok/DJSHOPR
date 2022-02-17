from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(verbose_name = "full manufacturer name",max_length = 255)
    slug = models.CharField(verbose_name = f"slug for manufacturer:{name}",max_length=255) # can do this ?
    class Meta:
        verbose_name = ("manufacturer")
        verbose_name_plural = ("manufacturers")
    def __str__():
        return f"manufacturer:{name}"