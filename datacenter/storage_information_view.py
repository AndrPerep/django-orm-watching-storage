from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        non_closed_visit = {
            'who_entered': visit.passcard,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)

