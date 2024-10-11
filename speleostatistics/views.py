import numpy as np
from django.shortcuts import render
from django.db.models import Avg
from django.db.models import Count
from caves.models import Cave
from caves.models import GEOMORPH_UNIT

# Create your views here.


def render_about(request):
    return render(request, 'speleostatistics/about.html')


def calculate_qf_percentiles():
    """
    Calculate cave metrics to QF caves (all caves).
    Returns results as dictionary to be show in index page.
    """
    total_caves = Cave.objects.count()

    percentiles = {}
    for field in ['length', 'depth', 'area', 'volume']:
        values = list(Cave.objects.values_list(
            field, flat=True).exclude(**{field: None}))

        if values:
            percentiles[field] = {
                '20th_percentile': round(np.percentile(values, 20), 2),
                '50th_percentile': round(np.percentile(values, 50), 2),
                '8x_50th': round(np.percentile(values, 50) * 8, 2)
            }

    return {
        'total_caves': total_caves,
        'percentiles': percentiles
    }


def calculate_geomorph_percentiles():
    """
    Calculate cave metrics to all caves in geomorphological units.
    Returns results as dictionary including count of caves.
    """
    result = {}
    geomorph_units = dict(GEOMORPH_UNIT)  # Usar a constante diretamente

    for geomorph_unit, unit_label in geomorph_units.items():
        caves_in_unit = list(Cave.objects.filter(
            geomorph_unit=geomorph_unit).values_list(
                'length', 'depth', 'area', 'volume'))

        cave_count = len(caves_in_unit)

        if cave_count > 0:
            unit_values = {
                'length': [cave[0] for cave in caves_in_unit],
                'depth': [cave[1] for cave in caves_in_unit],
                'area': [cave[2] for cave in caves_in_unit],
                'volume': [cave[3] for cave in caves_in_unit],
            }

            result[geomorph_unit] = {
                'unit_label': unit_label,
                'count': cave_count
            }

            for field in ['length', 'depth', 'area', 'volume']:
                if unit_values[field]:
                    percentile_20 = round(
                        np.percentile(unit_values[field], 20), 2)
                    percentile_50 = round(
                        np.percentile(unit_values[field], 50), 2)

                    result[geomorph_unit][field] = {
                        '20th_percentile': percentile_20,
                        '50th_percentile': percentile_50,
                        '8x_50th': round(percentile_50 * 8, 2)
                    }
        else:
            result[geomorph_unit] = {
                'unit_label': unit_label,
                'count': 0,
                'length': {},
                'depth': {},
                'area': {},
                'volume': {}
            }

    return result


def calculate_statistics():
    """
    Main function that returns the QF and geomorphological units percentiles.
    """
    qf_percentiles = calculate_qf_percentiles()
    geomorph_percentiles = calculate_geomorph_percentiles()

    return {
        'qf_percentiles': qf_percentiles,
        'geomorph_percentiles': geomorph_percentiles
    }


def display_statistics(request):
    """
    Renders the results in home view.
    """
    statistics = calculate_statistics()

    total_caves = Cave.objects.count()

    caves_by_geomorph = (
        Cave.objects
        .values('geomorph_unit')
        .annotate(count=Count('id'))
        .order_by('geomorph_unit')
    )

    context = {
        'statistics': statistics,
        'total_caves': total_caves,
        'caves_by_geomorph': caves_by_geomorph,
    }

    return render(request, 'speleostatistics/index.html', context)
