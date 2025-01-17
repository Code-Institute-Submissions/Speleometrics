from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from reports.models import Report
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

    return render(request, 'cave/table.html', context)


def cave_page(request, cave_name):
    """
    Retuns a cave page for the select page.
    Additionally, it allows logged-in users to
    report an inconsistency in cave data through a modal.
    """
    cave = get_object_or_404(Cave, cave_name=cave_name)

    if request.method == 'POST':
        if request.user.is_authenticated:
            inconsistency_details = request.POST.get('inconsistency_details')
            if inconsistency_details:
                Report.objects.create(
                    reported_by=request.user,
                    cave=cave,
                    cave_owner=cave.user,
                    inconsistency_details=inconsistency_details
                )

                return render(request, 'cave/cave_page.html', {
                    'cave': cave,
                    'success_message': "Report submitted successfully!"
                })
        else:
            return HttpResponseForbidden(render(request, '403.html', {
                'error_message': "You must be logged in to submit a report."
            }))

    return render(request, 'cave/cave_page.html', {'cave': cave})


@login_required
def add_cave(request, username):
    """
    Allows logged-in user to add a cave to Cave database
    """
    profile = get_object_or_404(Profile, user=request.user)

    if not profile.email_for_contact:
        return HttpResponseForbidden(
            render(
                request,
                '403.html',
                {
                    'error_message':
                        "To proceed, add an email for contact to your profile."
                }
            )
        )

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
            messages.success(
                request,
                "You have successfully added a new cave data!"
            )
            return redirect('cave_page', cave_name=cave.cave_name)
    else:
        form = CaveForm()
    return render(request, 'cave/add_cave.html', {'form': form})


@login_required
def edit_cave(request, username, cave_name):
    """
    Allows logged-in user or superusers to edit their cave registries.
    """

    cave = get_object_or_404(Cave, cave_name=cave_name)
    original_user = cave.user

    if request.user == cave.user or request.user.is_superuser:
        if request.method == 'POST':
            form = CaveForm(request.POST, request.FILES, instance=cave)
            if form.is_valid():
                cave = form.save(commit=False)
                cave.user = original_user
                if cave.relevance_surveyed == 1:
                    cave.relevance_factor = 0
                cave.save()
                messages.success(
                    request,
                    'You have successfully edited the cave data!')
                return redirect('cave_page', cave_name=cave.cave_name)
        else:
            form = CaveForm(instance=cave)
    else:
        return HttpResponseForbidden(
            render(request, '403.html', {
                'error_message':
                "You do not have permission to edit this cave."
            })
        )

    return render(request, 'cave/add_cave.html', {'form': form, 'cave': cave})


@login_required
def delete_cave(request, username, cave_name):
    """
    Allows logged-in user or superusers to delete their cave registries.
    """

    cave = get_object_or_404(Cave, cave_name=cave_name)

    if request.user == cave.user:
        cave.delete()
        context = {
            'message': "Cave deleted successfully."
        }
        return render(request, 'profiles/user_caves.html', context)

    elif request.user.is_superuser:
        cave.delete()
        context = {
            'message': "Cave deleted successfully."
        }
        return render(request, 'cave/table.html', context)

    else:
        return HttpResponseForbidden(render(request, '403.html', {
            'error_message': "You do not have permission to delete this cave."
        }))


def map_view(request):
    """
    Add caves to map page
    """
    caves = Cave.objects.all()
    context = {
        'caves': caves,
    }
    return render(request, 'cave/map.html', context)


# Adds custom 403 page to HttpResponseForbidden response
def custom_403_view(request, exception=None):
    """
    Renders custum 403 page
    """
    return render(request, '403.html', status=403)


# Adds custom 404 page
def custom_404_view(request, exception):
    """
    Renders custum 404 page
    """
    return render(request, '404.html', status=404)
