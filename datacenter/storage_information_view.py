from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import datetime

from datacenter.models import get_duration, format_duration, is_visit_long

def storage_information_view(request):
    currently_in_storage = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in currently_in_storage:
        name = visit.passcard
        entered_at = visit.entered_at
        duration = get_duration(visit)
        non_closed_visits.append({
            "who_entered": name,
            "entered_at": entered_at,
            "duration": format_duration(duration),
            "is_strange": is_visit_long(visit)
        })

    context = {
        "non_closed_visits": non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)



