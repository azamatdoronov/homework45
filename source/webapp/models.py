from django.db import models

# Create your models here.

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name="Описание")
    created_task = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    dead_line = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                              verbose_name="Статус")
    title = models.CharField(max_length=50, null=False, blank=False, default="No Title", verbose_name="Заголовок")

    def __str__(self):
        return f"{self.id}. {self.description}: {self.status} {self.dead_line}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
