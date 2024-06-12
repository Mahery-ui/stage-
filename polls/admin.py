from django.contrib import admin
from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)
# Register your models here.

class QuestionAdmin(admin, ModelAdmin):
    fields= ['pub_date', 'question_text']
admin.site.register(Question, QuestionAdmin)

class QuestionAdmin(admin, ModelAdmin):
    fieldsest= [
        (None,                {'fields': ['question_text']}), 
        ('Date information',  {'fields': ['pub_date']}), 
    ]
admin.site.register(Question, QuestionAdmin)