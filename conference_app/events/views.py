from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from events.models import Event, EventRegistration


# Create your views here.
class EventDetailView(DetailView):
    model = Event

class RegisterVisitorView(LoginRequiredMixin, View):

    def get(self, request, renginio_id):
        event = get_object_or_404(Event, id=renginio_id)

        registraciju_kiekis = EventRegistration.objects.filter(
            event = event, user = request.user).count()

        if registraciju_kiekis > 0:
            return HttpResponse ("Jus jau prisiregistravote!")

        registration = EventRegistration()
        registration.event = event
        registration.user = request.user
        registration.save()

        return redirect(f"/events/{renginio_id}")

class UserEventList( View ):
    def get( self, request ):

        if not request.user.is_authenticated:
            return redirect("login")

        user_events = EventRegistration.object.filter(
            user = request.user
        )

        return render(
            request,
            "events/user_events.html",
            { "object_list": user_events}
        )





