from django.db import models

class Response(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contactno = models.CharField(max_length=15)
    responsetype = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    responsetext = models.CharField(max_length=2000)
    posteddate = models.CharField(max_length=30)

    def __str__(self):
        return self.name