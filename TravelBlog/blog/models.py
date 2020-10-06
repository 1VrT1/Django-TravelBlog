from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Category(models.Model):
    name = models.CharField("Категория", max_length=40)
    url = models.SlugField(max_length=40, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Posts(models.Model):
    country = models.CharField("Страна", max_length=20)
    city = models.CharField("Город", max_length=20)
    title = models.CharField("Описание", max_length=120)
    poster = models.ImageField("Постер", upload_to='posters/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    is_public = models.BooleanField("Публичный доступ", default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    body = models.TextField("Описание", max_length=5000, blank=True)
    url = models.SlugField(max_length=130, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
