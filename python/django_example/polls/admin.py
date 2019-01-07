from django.contrib import admin
from .models import Question, Choice

# p.164

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # Change fields' order
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        # ('Date Information', {'fields': ['pub_date']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # View Choice model together
    list_display = ('question_text', 'pub_date') # Assign record columns
    list_filter = ['pub_date'] # Add side filter bar
    esarch_fields = ['question_text'] # Add search box

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)