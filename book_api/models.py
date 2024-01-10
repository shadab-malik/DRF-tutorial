from django.db import models

# Create your models here. here we create model that basically tells how our data will look like 
# and it autom. create a sql command that create table for us. 
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
