from django.db import models
from django.contrib.auth.models import AbstractUser
from account.managers import CustomUserManager
from ckeditor.fields import RichTextField
from django.db import models
from cloudinary.models import CloudinaryField

from PIL import Image


# Create your models here.

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),

)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)
    area_of_specialization = models.CharField(max_length=300, blank=True)
    bio = RichTextField()
    location = models.CharField(max_length=300, blank=True)
    # photo = CloudinaryField('photo', blank=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # def get_image(self):
    #     return self.photo

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/User.photo'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
    	os.remove(full_path)

    return profile_pic_name

