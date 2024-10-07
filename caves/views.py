from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from profiles.models import Profile
from .models import Cave
from .forms import CaveForm


def search_caves(request):
    """
    Returns caves according to sorting queries in a paginated view.
    Inspired by shop k-beauty developed by Joy Zadan.
    """
    caves = Cave.objects.all()
    query = request.GET.get('q', '')
    sortkey = request.GET.get('sort', 'cave_name')
    direction = request.GET.get('direction', 'asc')

    # Filtering
    if query:
        caves = caves.filter(
            Q(cave_name__icontains=query) | Q(description__icontains=query))

    # Sorting
    if sortkey in ['cave_name', 'user', 'length', 'depth', 'area', 'volume']:
        if sortkey == 'cave_name':
            caves = caves.annotate(
                lower_cave_name=Lower(
                    'cave_name')).order_by('lower_cave_name')
        elif sortkey == 'user':
            caves = caves.order_by('user__username')
        else:
            caves = caves.order_by(sortkey)

    # Sort Asceding or Descending order
    if direction == 'desc':
        caves = caves.order_by('-' + sortkey)

    # Pagination
    paginator = Paginator(caves, 20)
    page_number = request.GET.get('page')
    page_caves = paginator.get_page(page_number)

    context = {
        'caves': page_caves,
        'search_term': query,
        'current_sorting': f"{sortkey}_{direction}"}

    return render(request, 'cave/index.html', context)


def cave_page(request, cave_name):
    """
    Retuns a cave page for the select page
    """
    cave = get_object_or_404(Cave, cave_name=cave_name)

    return render(request, 'cave/cave_page.html', {'cave': cave})


@login_required
def add_cave(request, username):
    """
    Allows logged-in user to add a cave to Cave database
    """
    profile = get_object_or_404(Profile, user=request.user)

    if not profile.email_for_contact:
        return HttpResponseForbidden("""Please add an email for
         contact to your profile to proceed.""")

    if request.method == 'POST':
        form = CaveForm(request.POST, request.FILES)
        if form.is_valid():
            cave = form.save(commit=False)
            cave.user = request.user
            # if cave relevance was not surveyed legislation states
            # that relevance factor has to be considered maximum.
            if cave.relevance_surveyed == 1:
                cave.relevance_factor = 0
            cave.save()
            return redirect('profile_page', username=request.user.username)
    else:
        form = CaveForm()
    return render(request, 'cave/add_cave.html', {'form': form})


@login_required
def edit_cave(request, username, cave_name):
    """
    Allows logged-in user or superusers to edit their cave registries.
    """

    cave = get_object_or_404(Cave, cave_name=cave_name)

    if request.user == cave.user or request.user.is_superuser:
        if request.method == 'POST':
            form = CaveForm(request.POST, request.FILES, instance=cave)
            if form.is_valid():
                cave = form.save(commit=False)
                if cave.relevance_surveyed == 1:
                    cave.relevance_factor = 0
                cave.save()
                return redirect('cave_page', cave_name=cave.cave_name)
        else:
            form = CaveForm(instance=cave)
    else:
        return HttpResponseForbidden(
            "You do not have permission to edit this cave."
        )
    return render(request, 'cave/add_cave.html', {'form': form, 'cave': cave})


@login_required
def delete_cave(request, username, cave_name):
    """
    Allows logged-in user or superusers to delete their cave registries.
    """

    cave = get_object_or_404(Cave, cave_name=cave_name)

    if request.user == cave.user or request.user.is_superuser:
        cave.delete()
        return redirect('profile_page', username=request.user.username)
    else:
        return HttpResponseForbidden(
            "You do not have permission to delete this cave."
        )
