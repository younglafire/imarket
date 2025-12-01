from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal


class Guitar(models.Model):
    """Model for guitar products."""
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.TextField(blank=True)
    body_type = models.CharField(max_length=100, blank=True, help_text="e.g., Solid Body, Hollow Body, Semi-Hollow")
    pickup_configuration = models.CharField(max_length=50, blank=True, help_text="e.g., SSS, HSS, HH, SS")
    image1 = models.URLField(max_length=500, blank=True, help_text="URL for first product image")
    image2 = models.URLField(max_length=500, blank=True, help_text="URL for second product image")
    image3 = models.URLField(max_length=500, blank=True, help_text="URL for third product image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        ordering = ['-created_at']


class Fuzz(models.Model):
    """Model for fuzz pedal products."""
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.TextField(blank=True)
    fuzz_type = models.CharField(max_length=100, blank=True, help_text="e.g., Germanium, Silicon, Hybrid")
    image1 = models.URLField(max_length=500, blank=True, help_text="URL for first product image")
    image2 = models.URLField(max_length=500, blank=True, help_text="URL for second product image")
    image3 = models.URLField(max_length=500, blank=True, help_text="URL for third product image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Fuzzes"


class Amp(models.Model):
    """Model for amplifier products."""
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.TextField(blank=True)
    wattage = models.PositiveIntegerField(blank=True, null=True, help_text="Power output in watts")
    amp_type = models.CharField(max_length=100, blank=True, help_text="e.g., Tube, Solid-State, Hybrid, Modeling")
    image1 = models.URLField(max_length=500, blank=True, help_text="URL for first product image")
    image2 = models.URLField(max_length=500, blank=True, help_text="URL for second product image")
    image3 = models.URLField(max_length=500, blank=True, help_text="URL for third product image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Amplifier"
        verbose_name_plural = "Amplifiers"
