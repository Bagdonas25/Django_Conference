from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Conference, Like, Comment
from django.contrib import messages
from datetime import datetime


# Create your views here.
class ConferenceListView(ListView):
    model = Conference

class ConferenceDetailView(DetailView):
    model = Conference

class CreateCommentView( View, LoginRequiredMixin ):
    def post (self, request, pk):

        komentaro_tekstas = request.POST.get('komentaras')

        if len(komentaro_tekstas) == 0:
            messages.error( request, "Komentaras negali buti tuscias!")
            return redirect(f"/conferences/{pk}")
        #tikrinti nereikia naudojam LoginRequiredMixin

        # if request.user.is_authenticated == False:
        #     return HttpResponse("Klaida! Jums reikia prisijungti")

        konferencija = get_object_or_404( Conference, id=pk )

        komentaras = Comment()
        komentaras.author = request.user
        komentaras.conference = konferencija
        komentaras.comment = komentaro_tekstas
        komentaras.save()

        return redirect(f"/conferences/{pk}")

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

class CreateConferenceView(View):
    def get(self, request):
        return render(request, "conferences/conference_create.html")

    def post(self, request):
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        title = request.POST.get('title')

        if len(title) == 0:
            messages.error( request, "Butina ivesti pavadinima" )
            return redirect("/conference/new")

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            messages.error(request, "Blogai suvestos datos")
            return redirect("/conference/new")

        conference = Conference()
        conference.start_date = start_date
        conference.end_date = end_date
        conference.title = title
        conference.save()

        return redirect(f"/conferences/{conference.id}/")