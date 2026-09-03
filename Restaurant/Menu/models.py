from django.db import models
from pydantic import ValidationError


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

class itemImage(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def clean(self):
        super().clean()
        if not self.pk and self.item_id:
            current_count = self.item.images.count()
            if current_count >= 5:
                raise ValidationError("No puedes subir más de 5 imágenes para este producto.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Imagen de {self.item.name}"