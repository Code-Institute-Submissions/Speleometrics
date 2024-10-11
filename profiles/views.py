from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from caves.models import Cave
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
        return render(request, 'profiles/profile_page.html', {
         'profile': profile,
         'profile_user': profile_user})

    if profile.email_for_contact:
        return render(request, 'profiles/profile_page.html', {
            'profile': profile})
    return redirect(reverse('profile_edit', args=[profile_user.username]))


@login_required
def edit_profile(request, username):
    """
    Edit Profile
    """
    profile_user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=profile_user)

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


def user_search_caves(request, username):
    """
    Returns caves belonging to a specific user according
    to sorting queries in a paginated view.
    """
    # Get the user object based on the username from the URL
    user = get_object_or_404(User, username=username)

    # Filter caves by the user
    caves = Cave.objects.filter(user=user)

    # Search query and sorting parameters
    query = request.GET.get('q', '')
    sortkey = request.GET.get('sort', 'cave_name')
    direction = request.GET.get('direction', 'asc')

    # Filtering by search term (optional)
    if query:
        caves = caves.filter(
            Q(cave_name__icontains=query) | Q(description__icontains=query))

    # Sorting
    if sortkey in ['cave_name', 'length', 'depth', 'area', 'volume']:
        if sortkey == 'cave_name':
            caves = caves.annotate(
                lower_cave_name=Lower('cave_name')).order_by('lower_cave_name')
        else:
            caves = caves.order_by(sortkey)

    # Sort ascending or descending
    if direction == 'desc':
        caves = caves.order_by('-' + sortkey)

    # Pagination
    paginator = Paginator(caves, 20)
    page_number = request.GET.get('page')
    page_caves = paginator.get_page(page_number)

    context = {
        'caves': page_caves,
        'search_term': query,
        'current_sorting': f"{sortkey}_{direction}",
        'profile_user': user,
    }

    return render(request, 'profiles/user_caves.html', context)
