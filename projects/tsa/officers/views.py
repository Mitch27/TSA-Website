from django.shortcuts import render
from .models import Officer, Event, Sponsor
from django.http import HttpResponse

def officer_list(request):
	officers = Officer.objects.order_by('ordering')
	num_officer_list = int(len(officers)/6)
	if (len(officers) % 6 != 0):
		num_officer_list += 1
	officers = [officers[i*6:i*6+6] for i in xrange(num_officer_list)]
	events = Event.objects.order_by('event_date')[::-1][:12]
        sponsors = Sponsor.objects.order_by('ordering')[:12]

	data = {
		"officers": officers,
		"events": events,
		"sponsors": sponsors,
	}
	return render(request, 'officers/officer_list.html', data)

def underconstruction(request):
	return HttpResponse("Pardon the dust; Currently under construction")
