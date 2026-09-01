from django.db import models

# Create your models here.
class allergens(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Alergenos"
        verbose_name = "Alergeno"

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"

class item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    allergens = models.ManyToManyField(allergens)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Items"
        verbose_name = "Item"
