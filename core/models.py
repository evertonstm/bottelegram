from django.db import models

# Create your models here.


class Interaction(models.Model):
    input = models.CharField(max_length=100)
    output = models.TextField()
    code = models.TextField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return (self.input)

    class Meta:
        db_table = 'interaction'
