from django.db import models



class BinVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()

# Create your models here.
class Shoe(models.Model):
    manufacturer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture_url = models.TextField(null=True)

    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.PROTECT,
    )