from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
# from .forms import ProfileForm

# Create your views here.

def view_profile(request):
    """ 
    Retuns user profile 
    """
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('profiles/profile_edit.html') 
    return render(request, 'profiles/profile_page.html')

# Create your views here.

# @login_required
# def view_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile_page')
#     else:
#         form = ProfileForm()
#     return render(request, 'profile_edit', {'form': form})


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile_page')
#     else:
#         form = ProfileForm()
#     return render(request, 'profile_edit', {'form': form})
