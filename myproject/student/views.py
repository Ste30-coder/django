from django.shortcuts import render
from my_first_app.models import User, StudentProfile
from django.contrib.auth.decorators import login_required
# Create your views here.
def myhome(request):
    return render(request, "student/home.html")

@login_required
def edit_profile(request):
    if request.method == 'POST':
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        course = request.POST.get('course')
        duratio = request.POST.get('duration')
        
        print(request.user.id," ------hello----- ")
        # user = User.objects.get(id=request.user.id)
        
        # student_profile = StudentProfile.objects.get(user=request.user)
        # student_profile.phone = phone
        # student_profile.save()
        
        # student_profile = StudentProfile.objects.get(user__id=request.user.id)
        
        StudentProfile.objects.create(
            user=request.user,
            course=course,
            duration=duratio
        )
        return render(request, 'student/home.html')
    else:
        return render(request, 'student/edit_profile.html')