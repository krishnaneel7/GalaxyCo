from django.db import models


class CustomerRequest(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Contacted", "Contacted"),
        ("Completed", "Completed"),
    ]


    name = models.CharField(
        max_length=100
    )


    email = models.EmailField()


    phone = models.CharField(
        max_length=20
    )


    product = models.CharField(
        max_length=200
    )


    quantity = models.PositiveIntegerField(
        default=1
    )


    message = models.TextField(
        blank=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.name} - {self.product}"