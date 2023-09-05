from django.db import models

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=30)
    roll_no=models.IntegerField()

    def __str__(self):
        return self.name
    
class Upload_Item(models.Model):
    item_name=models.CharField(max_length=244)
    item_price=models.PositiveIntegerField()
    u_image=models.FileField(upload_to="images/", max_length=100 , null=True , default="")


    def __str__(self):
        return self.item_name
    

    