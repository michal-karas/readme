# Generated by Django 3.0.5 on 2020-05-09 14:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('pub_data', models.DateTimeField(blank=True, null=True, verbose_name='Publication timestamp')),
                ('state', models.CharField(choices=[('draft', 'Draft'), ('in_moderation', 'In-moderation'), ('rejected', 'Rejected'), ('published', 'Published')], max_length=40, verbose_name='Title')),
                ('grade', models.PositiveIntegerField(help_text='Values from 1 to 10', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)], verbose_name='Grade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveIntegerField(help_text='Values from 1 to 10', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)], verbose_name='Grade')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
