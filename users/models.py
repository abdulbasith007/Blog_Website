from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    usr=models.OneToOneField(User,on_delete=models.CASCADE)
    Image=models.ImageField(default='Profile_Pics/default.jpg',upload_to='Profile_Pics')

    def save(self,*args,**kwargs):
        super().save()
        print(self.Image.path)
        img=Image.open(self.Image.path)
        if img.height>300 or img.width>300:
            op_size=(300,300)
            img.thumbnail(op_size)
            img.save(self.Image.path)
            print(self.Image.path)