from django.core.paginator import Paginator
from django.shortcuts import render
# from django.views import generic
from .models import Cave

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
 