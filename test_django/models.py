from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(**kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Team(models.Model):
    number = models.CharField(max_length=20, verbose_name="Номер команды",
                              help_text="Введите номер команды", null=False, blank=False)

    # course = IntegerRangeField(min_value=1, max_value=5, verbose_name="Номер курса", help_text="Введите номер курса", null=False, blank=False)

    def __str__(self):
        return self.number

    class Meta:
        db_table = "Team"
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Department(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name="Название отдела",
                            help_text="Введите название отдела", null=False, blank=False)
    description = models.TextField(verbose_name="Описание отдела", help_text="Введите описание отдела")

    # teams .= models.ManyToManyField(Team)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Department"
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Worker(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя",
                                  help_text="Введите имя", null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия",
                                 help_text="Введите фамилию", null=False, blank=False)
    date_birth = models.DateField(verbose_name="Дата рождения",
                                  help_text="Введите дату рождения", null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Номер команды",
                             help_text="Выберете номер команды", null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="id пользователя",
                                help_text="Выберите id пользователя", null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "Worker"
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Leader(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя",
                                  help_text="Введите имя", null=False, blank=False)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия",
                                 help_text="Введите фамилию", null=False, blank=False)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Название отдела",
    #                                help_text="Выберите отдел", null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="id пользователя",
                                help_text="Выберите id пользователя", null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "Leader"
        verbose_name = 'Тимлид'
        verbose_name_plural = 'Тимлиды'


class Project(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name="Название проекта",
                            help_text="Введите название проекта", null=False, blank=False)
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE, verbose_name="Тимлид",
                               help_text="Выберите тимлида", null=False, blank=False)
    team = models.ManyToManyField(Team)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Project"
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    number = IntegerRangeField(min_value=0, default=1, verbose_name="Номер задания",
                               help_text="Введите номер задания", null=False, blank=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Работник",
                               help_text="Выберите работника", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект",
                                help_text="Выберите проект", null=True, blank=True, db_column="project")
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Отдел",
    #                                help_text="Выберите отдел", null=True, blank=True, default="Отдел backend-разработки",
    #                                db_column="department")
    task_status = IntegerRangeField(min_value=0, max_value=1, default=0,
                                    verbose_name="Статус задания (1 - задание выполнено, 0 - задание не выполнено)",
                                    help_text="Введите текущий статус задания: 0 или 1", null=False, blank=False)
    date_control = models.DateTimeField(verbose_name="Дата и время сдачи",
                                        help_text="Выберете дату и время сдачи", null=False, blank=False)

    # file = models.FileField()

    def __str__(self):
        return "Сдал: " + self.worker.__str__() + ". Статус: " + self.task_status.__str__()

    class Meta:
        db_table = "Task"
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
