from django.db import models

# Create your models here.
#Campos de la BBDD

#Si accedemos a localhost/admin veremos la nueva tabla creada.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title