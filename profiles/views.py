from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm

# Create your views here.

@login_required
def view_profile(request, username):
    """ 
    Returns user profile, if contact email is empity return edit profile form.
    """
    profile_user = get_object_or_404(User, username=username)

    profile = get_object_or_404(Profile, user=profile_user)

    if request.user != profile_user:
        return render(request, 'profiles/profile_page.html', {'profile': profile})

    if profile.email_for_contact:
        return render(request, 'profiles/profile_page.html', {'profile': profile})
    return redirect(reverse('profile_edit', args=[profile_user.username]))

@login_required
def edit_profile(request, username):
    """ 
    Edit Profile
    """
def edit_profile(request, username):
    """ 
    Edit Profile
    """
    profile_user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=profile_user)

    print("Profile Data:")
    print(f"Display Name: {profile.display_name}")
    print(f"Email for Contact: {profile.email_for_contact}")
    print(f"Profile Type: {profile.profile_type}")
    print(f"Bio: {profile.bio}")

    # Fix - Bug03 - permission access edit profile through typing the link
    if request.user != profile_user:
        return redirect('home')

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page', username=profile_user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/profile_edit.html', {'form': form})
