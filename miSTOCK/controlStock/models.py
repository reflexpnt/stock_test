from django.db import models

# Create your models here.
class Componente(models.Model):

    STATUS_ORDERABLE = 1
#    compoManufacturer =  models.ForeignKey('auth.User')
    PartNum     = models.CharField(max_length=20)
    Description = models.CharField(max_length=200)
    Datasheet   = models.CharField(max_length=200, blank=True, null=True)
    Stock       = models.CharField(max_length=200)
    Price       = models.DecimalField(max_digits=10, decimal_places=4)

    def is_orderable(self):
        return self.status in Componente.STATUS_ORDERABLE

    def __str__(self):
        #return '%s' % (format_part_number(self.id))
        return self.PartNum
