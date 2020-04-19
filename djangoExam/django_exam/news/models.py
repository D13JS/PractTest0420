from django.db import models
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class report(models.Model):
    report_title = models.CharField(max_length = 200)
    report_body = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.report_title