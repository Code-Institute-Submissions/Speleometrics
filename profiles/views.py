from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_page')
    else:
        form = ProfileForm()
    return render(request, 'profile_edit', {'form': form})
