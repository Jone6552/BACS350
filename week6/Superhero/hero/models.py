from django.db import models


class Hero (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self)
        return reverse_lazy('hero_detail', args=[str(self.id)])