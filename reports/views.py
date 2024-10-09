from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import  get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Report
from .forms import ReportForm

# Create your views here.

def search_report(request):
    """
    Returns reports according to sorting queries in a paginated view.
    """

    if request.user.is_superuser:
        reports = Report.objects.all()
        query = request.GET.get('q', '')
        sortkey = request.GET.get('sort', 'cave__cave_name')
        direction = request.GET.get('direction', 'asc')

        # Filtering
        if query:
            reports = reports.filter(
                Q(cave__cave_name__icontains=query) |
                Q(inconsistency_details__icontains(query)) |
                Q(reported_by__username__icontains(query)) |
                Q(cave_owner__username__icontains(query))
            )

        # Sorting
        if sortkey in ['cave__cave_name', 'reported_by', 'cave_owner',
         'reported_created_date']:
            if sortkey == 'cave__cave_name':
                reports = reports.annotate(
                    lower_cave_name=Lower(
                        'cave__cave_name')).order_by('lower_cave_name')
            elif sortkey == 'reported_by':
                reports = reports.order_by('reported_by__username')
            elif sortkey == 'cave_owner':
                reports = reports.order_by('cave_owner__username')
            elif sortkey == 'reported_created_date':
                reports = reports.order_by('reported_created_date')
            else:
                reports = reports.order_by(sortkey)

        # Sort Ascending or Descending order
        if direction == 'desc':
            reports = reports.order_by('-' + sortkey)

        # Pagination
        paginator = Paginator(reports, 8)
        page_number = request.GET.get('page')
        page_reports = paginator.get_page(page_number)

        context = {
            'reports': page_reports,
            'search_term': query,
            'current_sorting': f"{sortkey}_{direction}",
        }

        return render(request, 'reports/reports.html', context)   

    else:
        return HttpResponseForbidden
        (render(request, '403.html', {
             'error_message':
                "You do not have permission to access this page."
                }))


def delete_report(request, id):
    """
    Allows superuser to delete a report.
    """

    report = get_object_or_404(Report, id=id)

    if request.user.is_superuser:
        report.delete()
        messages.success(
            request, 'You have successfully deleted a report!')
        return redirect('reports_index')
    else:
        return HttpResponseForbidden
        (render(request, '403.html', {
             'error_message':
                "You do not have permission to access this page."
                }))


def report_page(request, id):
    """
    Retuns a report page that displays the report general information.
    """
    report = get_object_or_404(Report, id=id)

    if request.method == 'GET':
        return render(request, 'reports/reports_page.html', {
            'report': report
        })

