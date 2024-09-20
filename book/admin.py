from django.contrib import admin
from .models import Plane, Flight, PlaneSeat, Passenger

admin.site.register(Plane)
admin.site.register(Flight)
admin.site.register(PlaneSeat)
admin.site.register(Passenger)