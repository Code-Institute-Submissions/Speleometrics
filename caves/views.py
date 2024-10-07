from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from profiles.models import Profile
from .models import Cave
from caves.forms import CaveForm

def cave_list_table(request):
    """
    Retuns all caves in a paginated view
    """
    cave_list = Cave.objects.all()
    paginate_by = Paginator(cave_list, 50)

    page_number = request.GET.get('page')
    page_obj = paginate_by.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'is_paginated': paginate_by.num_pages > 1,
    }

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
            """if cave relevance was not surveyed legislation states
             that relevance factor has to be considered maximum."""
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
                cave.user = request.user or superusers
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
    return render(request, 'cave/add_cave.html', {'form': form,
     'cave': cave})


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
