from django.db import models



class LocationVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    closet_name = models.CharField(max_length=100)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()


class Hat(models.Model):
    fabric = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    url = models.TextField(null=True)
    location = models.ForeignKey(
        LocationVO ,
        related_name="+",
        on_delete=models.PROTECT,

    )







# class Location(models.Model):
#     closet_name = models.CharField(max_length=100)
#     section_number = models.PositiveSmallIntegerField()
#     shelf_number = models.PositiveSmallIntegerField()

#     def get_api_url(self):
#         return reverse("api_location", kwargs={"pk": self.pk})

#     def __str__(self):
#         return f"{self.closet_name} - {self.section_number}/{self.shelf_number}"

#     class Meta:
#         ordering = ("closet_name", "section_number", "shelf_number")