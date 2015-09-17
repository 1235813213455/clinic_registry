from datetime import datetime, timedelta

from django.shortcuts import render, render_to_response, get_object_or_404

from registry.models import Doctor, Assignment

def index(request):
    doctors = Doctor.objects.all()
    return render_to_response('doctors/index.html', {'doctors': doctors})

def doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    today = datetime.now()
    seven_days_later = today + timedelta(days=7)
    week_assignment_cursor = Assignment.objects \
                .filter(doctor__id=doctor_id) \
                .filter(date__gte=today) \
                .filter(date__lt=seven_days_later)

    week_assignments = {}
    for assignment in week_assignment_cursor:
        date = assignment.date.strftime("%Y/%m/%d")
        if not week_assignments.get(date, None):
            week_assignments[date] = set([])

        week_assignments[date].add(assignment.time)

    print(week_assignments)

    days = []
    for i in range(7):
        day = {}
        current_day = (today + timedelta(days=i)).strftime('%Y/%m/%d')
        day["date"] = current_day
        day["hours"] = []
        days.append(day)
        for hour_id in Assignment.HOUR_MAP.keys():
            occupied = True if week_assignments.get(current_day, None) \
                                and hour_id in week_assignments[current_day] else False
            day["hours"].append({"time": Assignment.HOUR_MAP[hour_id], 
                                "occupied": occupied})
        day["hours"].sort(key=lambda x: x["time"]["id"])

    return render_to_response('doctors/doctor.html', {'days': days, "doctor": doctor})
