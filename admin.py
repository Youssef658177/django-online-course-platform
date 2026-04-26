from django.contrib import admin
from .models import Course, Lesson, Question, Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'course', 'grade']
    list_filter = ['course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
