import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from.models import Course, Level, Lesson, Question
# Create your views here.


def start(request):
    return redirect("/courses")


def error(request):
    return render(request, "pages/error.html")


def home(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "pages/courses.html", context)


@login_required
def course(request, id):
    crs = Course.objects.get(id=id)
    levels = Level.objects.filter(course=crs)
    first_level = get_object_or_404(levels, first_level=True)
    if crs not in request.user.profile.courses.all():
        request.user.profile.courses.add(crs)
        request.user.profile.levels.add(first_level)
        lessons = Lesson.objects.filter(level=first_level)
        first_lesson = get_object_or_404(lessons, first_lesson=True)
        request.user.profile.lessons.add(first_lesson)
    else:
        pass
    context = {
        "course": crs,
        "levels": levels
    }
    return render(request, "pages/course.html", context)


@login_required
def question(request, id):
    level = Level.objects.get(id=id)
    questions = Question.objects.filter()
    random_question = random.choice(questions)
    real_answer = random_question.answer
    context = {
        "question": random_question
    }
    # Process answer
    if request.method == "POST":
        user_answer = request.POST["option"]
        if user_answer == real_answer:
            request.user.profile.levels.add(level.nxt)
            lessons = Lesson.objects.filter(level=level.nxt)
            first_lesson = get_object_or_404(lessons, first_lesson = True)
            request.user.profile.lessons.add(first_lesson)
            return redirect(f"/level/{level.nxt.id}")
        else:
            return redirect(f"/level/{level.id}")
    if level in request.user.profile.levels.all():
        return render(request, "pages/quiz.html", context)
    else:
        return redirect("/error")


@login_required
def level(request, id):
    lvl = Level.objects.get(id=id)
    if lvl not in request.user.profile.levels.all():
        lessons = Lesson.objects.filter(level=lvl)
        context = {
            "level": lvl,
            "lessons": lessons
        }
        return render(request, "pages/lessons.html", context)
    else:
        return redirect("/error")


@login_required
def level(request, id):
    lvl = Level.objects.get(id=id)
    if lvl in request.user.profile.levels.all():
        lessons = Lesson.objects.filter(level=lvl)
        context = {
            "level": lvl,
            "lessons": lessons
        }
        return render(request, "pages/lessons.html", context)
    else:
        return redirect("/error")


@login_required
def watch(request, id):
    lesson = Lesson.objects.get(id=id)
    if lesson not in request.user.profile.lessons.all():
        request.user.profile.lessons.add(lesson)
    else:
        pass

    context = {
        "lesson": lesson
    }
    return render(request, "pages/Lesson.html", context)