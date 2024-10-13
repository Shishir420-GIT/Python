from django.db import models

# Create your models here.

class Destination:
    def __init__(self, id, name, description, image_url, price):
        self.id = id
        self.name = name
        self.description = description
        self.image_url = image_url
        self.price = price
    