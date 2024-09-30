from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.

@login_required
def view_profile(request):
    """ 
    Returns user profile, if contact email is empity return edit profile form.
    """
    profile = get_object_or_404(Profile, user=request.user)
    
    if not profile.email_for_contact:
        return redirect('profile-edit')
    return render(request, 'profiles/profile_page.html', {'profile': profile})


def edit_profile(request):
    """ 
    Edit Profile
    """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})
