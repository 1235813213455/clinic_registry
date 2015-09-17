from datetime import datetime, timedelta

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect

from registry.models import Doctor, Patient, Assignment
from registry.forms import RegisterForm 

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
        day["raw_date"] = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        day["hours"] = []
        days.append(day)
        for hour_id in Assignment.HOUR_MAP.keys():
            occupied = True if week_assignments.get(current_day, None) \
                                and hour_id in week_assignments[current_day] else False
            day["hours"].append({"time": Assignment.HOUR_MAP[hour_id], 
                                "occupied": occupied})
        day["hours"].sort(key=lambda x: x["time"]["id"])

    return render_to_response('doctors/doctor.html', {'days': days, "doctor": doctor})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            doctor = get_object_or_404(Doctor, pk=form.cleaned_data["doctor_id"])
            assignment_date = datetime.strptime(form.cleaned_data["assignment_date"], "%Y-%m-%d")
            assignment_time = [v for v in Assignment.HOUR_MAP.values() if v["range"] == form.cleaned_data["assignment_time"]][0]

            patient = Patient()
            patient.first_name = form.cleaned_data["first_name"]
            patient.second_name = form.cleaned_data["second_name"]
            patient.father_name = form.cleaned_data["father_name"]
            patient.save()

            #check if assignment already registered
            num_results = Assignment.objects.filter(doctor__id=doctor.id) \
                                            .filter(date=assignment_date) \
                                            .filter(time=assignment_time["id"]) \
                                            .count()

            if num_results > 0:
                return HttpResponseRedirect('/registry/time_occupied_error/')
            else:
                new_assignment = Assignment()
                new_assignment.doctor = doctor
                new_assignment.patient = patient
                new_assignment.date = assignment_date
                new_assignment.time = assignment_time["id"]
                new_assignment.save()
            
                return HttpResponseRedirect('/registry/' + str(doctor.id) + '/')
    else:
        doctor_id = request.GET.get("doctor", -1)
        doctor = get_object_or_404(Doctor, pk=doctor_id)

        time_id = request.GET.get("time", -1)
        time = Assignment.HOUR_MAP.get(int(time_id), None)["range"]

        date = request.GET.get("date", -1)
        form = RegisterForm(initial={'doctor_id': doctor.id, 'doctor_name': doctor.name, 
                             'assignment_date': date, 'assignment_time': time})

    return render(request, 'doctors/register_form.html', {'form': form})

def time_occupied(request):
    return render_to_response('doctors/time_occupied.html')
