from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from books.models import Book


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Author",
        help_text='',
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Title",
        help_text=''
    )
    content = models.TextField(
        blank=False,
        verbose_name="Content",
        help_text='',
    )
    pub_data = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Publication timestamp",
        help_text='',
    )
    STATE_CHOICES = (
        ('draft', 'Draft'),
        ('in_moderation', 'In-moderation'),
        ('rejected', 'Rejected'),
        ('published', 'Published'),
    )
    state = models.CharField(
        choices=STATE_CHOICES,
        max_length=40,
        null=False,
        blank=False,
        verbose_name="Title",
        help_text='',
    )
    grade = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name="Grade",
        help_text='Values from 1 to 10',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(11),
        ],
    )

class Grade(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Author",
        help_text="",
    )
    grade = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name="Grade",
        help_text="Values from 1 to 10",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(11),
        ],
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Book",
        help_text="",
    )
