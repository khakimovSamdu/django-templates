from django.db import models

# Create your models here.
class Smartphone(models.Model):
    name = models.CharField(max_length = 56)
    company = models.CharField(max_length = 16)
    color = models.CharField(max_length = 24)
    RAM = models.CharField(max_length = 24)
    memory = models.CharField(max_length = 36)
    price = models.FloatField()
    img_url = models.CharField(max_length = 156)
    
    def __str__(self) -> str:
        return self.name
    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "company": self.company,
            "color": self.color,
            "RAM": self.RAM,
            "memory": self.memory,
            "price": self.price,
            "img_url": self.img_url,
        }