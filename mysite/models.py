from django.db import models

# Create your models here.


class Services(models.Model):
    service_name = models.CharField(max_length=200)
    service_description = models.TextField()
    service_img = models.ImageField()

    class Meta:
        verbose_name_plural = "Services"


class Projects(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    project_img = models.ImageField()
    project_link = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Projects"


class Queries(models.Model):
    customer_name = models.CharField(max_length=150)
    customer_email = models.EmailField(max_length=254)
    customer_query = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Queries"


class GokulaKannan(models.Model):
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "GokulaKannan"
