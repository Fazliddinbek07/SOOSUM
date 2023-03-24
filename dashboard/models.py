from django.db import models

class Info(models.Model):
    logo = models.ImageField(null=True, blank=True, upload_to="logo/")
    text_uz = models.TextField()
    text_ru = models.TextField()

    def __str__(self):
        return self.text_uz + " " + self.text_ru

class SocialMedia(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="social_media/")
    link = models.URLField()

    def __str__(self):
        return self.link

class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " " + self.phone

class Discount(models.Model):
    img = models.ImageField(blank=True, null=True, upload_to="discount/")

class Product(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="product/")
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)

    def __str__(self):
        return self.name_uz + " " + self.name_ru

class AboutProduct(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to="about_product/")

class About(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to="about/")

class WhoUse(models.Model):
    text_uz = models.TextField()
    text_ru = models.TextField()

    def __str__(self):
        return self.text_uz + " " + self.text_ru

class HowToUse(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()
    img = models.ImageField(null=True, blank=True)

class Fact(models.Model):
    number = models.CharField(max_length=255)
    text_uz = models.TextField()
    text_ru = models.TextField()