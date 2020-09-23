from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Priority(models.Model):
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, "Высокий приоритет"),
        (PRIORITY_MEDIUM, "Средний приоритет"),
        (PRIORITY_LOW, "Низкий приоритет"),
    ]

    prior = models.IntegerField("Важность", choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM)
    todos_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Важность'
        verbose_name_plural = 'Важность'

    def __str__(self):
        PRIORITY_CHOICES = {
            1:"Высокий приоритет",
            2:"Средний приоритет",
            3:"Низкий приоритет"
        }
        return PRIORITY_CHOICES[self.prior]


class Category(models.Model):
    slug = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    todos_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return "{} {}".format(self.name, self.todos_count)


class TodoItem(models.Model):
    description = models.TextField("описание")
    is_completed = models.BooleanField("выполнено", default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="task_priority")
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("tasks:details", args=[self.pk])

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'