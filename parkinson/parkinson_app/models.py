from django.db import models
from django.utils import timezone
# Create your models here.


class ParkinsonModel(models.Model):
    ppe = models.FloatField(default=0)
    shimmerapq5 = models.FloatField(default=0)
    mdvpfo = models.FloatField(default=0)
    mdvpshimmer = models.FloatField(default=0)
    mdvpfhi = models.FloatField(default=0)
    mdvpflo = models.FloatField(default=0)
    rpde = models.FloatField(default=0)
    is_parkinson = models.BooleanField(default=False)

    created_date = models.DateField(default=timezone.now)

    def to_dict(self):
        return {'PPE': self.ppe, 'Shimmer_APQ5':self.shimmerapq5, 'MDVP_FO':self.mdvpfo, 'MDVP_Shimmer':self.mdvpshimmer, 'MDVP_Fhi':self.mdvpfhi, 'MDVP_Flo':self.mdvpflo, 'RPDE':self.rpde, 'created_date':self.created_date, 'is_parkinson':self.is_parkinson}