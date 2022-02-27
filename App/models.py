from django.db import models

# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length=100,verbose_name="имя_фамилия")
    email = models.CharField(max_length=100,verbose_name="почта")
    work1 = models.CharField(max_length=100,blank=True, null=True)
    work2 = models.CharField(max_length=100,blank=True, null=True)
    work3 = models.CharField(max_length=100,blank=True, null=True)
    work4 = models.CharField(max_length=100,blank=True, null=True)
    work5 = models.CharField(max_length=100,blank=True, null=True)
    work6 = models.CharField(max_length=100,blank=True, null=True)
    # price = models.IntegerField()
    # description = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='shop/image' , null=True , blank=True)
    
    def __str__(self):
        return self.name
    def str(self):
        return self.name
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

class Myworks(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image' , null=True , blank=True)
    link=models.CharField(max_length=1000)
    title = models.CharField(max_length=255)

    
    # price = models.IntegerField()
    # description = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='shop/image' , null=True , blank=True)
    
    def __str__(self):
        return self.name
    def str(self):
        return self.name