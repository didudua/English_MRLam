from django import forms
from english.models import Exercise, Course, Lesson


class KhoaHocForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']
        widgets = {
            'course_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tên khóa học'
            }),
        }
class BuoiHocForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_name', 'description', 'lesson_file', 'exercise_file']
        widgets = {
            'lesson_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tên bài học'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập mô tả bài học'
            }),
            'lesson_file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tải lên file bài học'
            }),
            'exercise_file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tải lên file bài tập'
            }),
        }

