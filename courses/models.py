from django.db import models

# Create your models here.


class Course(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="course_covers")
    title = models.CharField(max_length=500)
    def __str__(self):
        return str(self.title)



class Level(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to="level_covers")
    nxt = models.ForeignKey("Level", on_delete=models.CASCADE, null=True, blank=True)
    has_next = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    first_level = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class Lesson(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    img = models.ImageField(upload_to="Lesson_covers")
    url = models.URLField()
    nxt = models.ForeignKey("Lesson", on_delete=models.CASCADE, null=True, blank=True)
    has_next = models.BooleanField(default=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    first_lesson = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)


class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    lvl = models.ForeignKey(Level, on_delete=models.CASCADE)
    op1 = models.CharField(max_length=500)
    op2 = models.CharField(max_length=500)
    op3 = models.CharField(max_length=500)
    op4 = models.CharField(max_length=500)

    def __str__(self):
        return str(self.question)