from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
import uuid

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    
    def get_file_path(instance, filename):
        
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.user.username.lower() + "_" + str(uuid.uuid4()), ext)
        return os.path.join('profile_images', filename)
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    avatar = models.ImageField(default='default.jpg', upload_to= get_file_path)
    bio = models.TextField(default="I am new")
    phone_number = models.TextField(default=None)
    user_cv  = models.FileField(default='default.png', upload_to='doc')
    kind = models.IntegerField(default='J')
    
    

    def __str__(self):
        
        return self.user.username
    
    def save(self, *args, **kwargs):

        super().save()
        
        img = Image.open(self.avatar.path)
        #os.remove(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
        
  
            
    '''
    def content_file_name(self, *args, **kwargs):
        ext = self.avatar.path.split('.')[-1]
        filename = "%s.%s" % (self.user.suername, ext)
        return os.path.join('uploads', filename)
    '''