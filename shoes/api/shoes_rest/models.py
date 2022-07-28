from django.db import models
from django.urls import reverse


class BinVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    closet_name = models.CharField(max_length=100)


# Create your models here.
class Shoe(models.Model):
    manufacturer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.TextField(null=True)

    bin = models.ForeignKey(
        BinVO,
        related_name="bin",
        on_delete=models.PROTECT,
    )

    def get_api_url(self):
        return reverse("api_list_shoes", kwargs={"pk": self.pk})