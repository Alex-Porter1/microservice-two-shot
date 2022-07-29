from django.db import models
from django.urls import reverse

# Create your models here.
class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()
    import_href = models.CharField(max_length=200, unique=True, null=True)

class Shoe(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    picture_url = models.URLField()
    bin = models.ForeignKey(BinVO, related_name="shoes", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def get_api_url(self):
        return reverse("api_shoe", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("bin",)
