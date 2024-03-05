from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Create your models here.

class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True,
                                        null=True)  # autonowadd giúp ngừi ta thêm dữ liệu lấy thời điểm đó
    updated_date = models.DateTimeField(auto_now=True, null=True)  # cập nhật lại thời điểm đó
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True, blank=True)
    description = RichTextField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
