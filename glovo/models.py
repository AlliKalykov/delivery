from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    message = models.TextField()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-name', )

    def get_name_and_email(self):
        return f'{self.name} {self.email}'
    