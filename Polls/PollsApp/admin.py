from django.contrib import admin
from .models import *


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionForm(admin.ModelAdmin):
    list_display= ['id', 'question_text', 'pub_date']
    list_display_links = []
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date and Time', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]


class ChoiceForm(admin.ModelAdmin):
    list_display= ['id', 'question', 'choice_text', 'votes']
    list_display_links = []


admin.site.register(Question, QuestionForm)
admin.site.register(Choice, ChoiceForm)