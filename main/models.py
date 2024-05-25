from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=123)
    phone = models.CharField(max_length=123)

    def __str__(self):
        return f'Заявка от: {self.name} - {self.email}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
