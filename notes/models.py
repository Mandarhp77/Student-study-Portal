from django.db import models
from django.forms import forms
from django.forms import widgets

class Notes(models.Model):
    title=models.CharField(max_length=50)
    description =models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Notes"

class Homework(models.Model):
    title=models.CharField(max_length=50)
    status =models.BooleanField(default = False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Homework"

class Todo(models.Model):
    title=models.CharField(max_length=50)
    todostatus =models.BooleanField(default = False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Todo"

