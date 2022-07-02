from django.db import models
from django.utils.translation import ugettext_lazy as _

from frontend.models import BaseModel

# Create your models here.

class Bitcoin(BaseModel):
    symbol = models.CharField(_("Symbol"), max_length=100, default="BTCUSDT")
    price = models.IntegerField(_("Price"), default=0)
    
    @property
    def timestamp(self):
        return self.created_on.timestamp()
    
    class Meta:
        ordering = ['-created_on']