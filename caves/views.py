from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from profiles.models import Profile
from .models import Cave
from caves.forms import CaveForm

# Create your views here.

# class CaveList(generic.ListView):
#     """
#     Retuns all caves in a paginated view
#     """
#     queryset = Cave.objects.all()
#     template_name = "cave/index.html"
#     paginate_by = 50

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


@login_required
def add_cave(request):
    """
    Allows the logged-in user to add a cave to Cave database
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
