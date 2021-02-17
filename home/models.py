from django.db import models

class Person(models.Model):
        name = models.CharField(max_length=30)
        email = models.EmailField(max_length=30,null=True)
        desc = models.TextField()

        def __str__(self):
                return self.name