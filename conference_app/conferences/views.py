from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Conference, Like


# Create your views here.
class ConferenceListView(ListView):
    model = Conference

class ConferenceDetailView(DetailView):
    model = Conference

class ConferenceLikeView(View):
    def get(self, request,konferencijos_id ):
        if not request.user.is_authenticated:
            return redirect ("login")

        conference = get_object_or_404(Conference, id= konferencijos_id)

        like_kiekis = Like.objects.filter(
            conference=conference, user=request.user).count()

        if like_kiekis > 0:
            return HttpResponse("Jus jau prisiregistravote!")

        registration = Like()
        registration.conference = conference
        registration.user = request.user
        registration.save()
        return redirect("conference-detail", konferencijos_id)

