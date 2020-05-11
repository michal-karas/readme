from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="First Name",
        help_text="",
    )
    last_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Last Name",
        help_text="",
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Birth Date",
        help_text="",
    )
    web_site = models.URLField(
        null=False,
        blank=False,
        verbose_name="Web Site",
        help_text="",
    )


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Title",
        help_text="",
    )
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Author",
        help_text="",
    )
    categories = models.ManyToManyField(
        "Category",
        blank=False,
        verbose_name="Categories",
        help_text="",
    )
    pages = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Pages",
        help_text="",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="",
    )

    # cover_link = models.ImageField(
    # )
    # link do zdjęcia książki


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Category Name",
        help_text="",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description",
        help_text="",
    )
