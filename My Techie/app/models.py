from django.db import models
from datetime import datetime,timedelta
class Posts(models.Model):
    file=models.FileField(upload_to='posts',default=None)
    txt=models.TextField(default=datetime.now())
    my_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    img=models.ImageField(upload_to='photos',default=None)
