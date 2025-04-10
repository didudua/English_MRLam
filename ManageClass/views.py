from django.shortcuts import render, get_object_or_404, redirect
from english.models import Class, UserClass, UserProfile, Course
from .forms import ClassForm  # Nếu bạn tạo form cho thêm lớp

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})

def class_detail(request, class_id):
    class_instance = get_object_or_404(Class, pk=class_id)
    user_classes = UserClass.objects.filter(class_instance=class_instance).select_related('user')
    return render(request, 'class_detail.html', {
        'class_instance': class_instance,
        'user_classes': user_classes
    })

def class_rollcall(request, class_id):
    # logic hiển thị điểm danh (theo ảnh bạn gửi)
    pass

def add_student_to_class(request, class_id):
    # logic thêm học sinh vào lớp
    pass

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'add_class.html', {'form': form})
