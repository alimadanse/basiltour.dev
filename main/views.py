from django.shortcuts import render, get_object_or_404
from .models import Tour,TourRegistration
from .forms import TourForm, TourRegisterForm
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView


class TourDetailView(generic.DetailView):
    model = Tour
    template_name = 'tour_detail.html'
    context_object_name = "tour"


class TourListView(generic.ListView):
    model = Tour
    template_name = 'tour_list.html'
    context_object_name = 'tours'


def home(request):
    return render(request, 'home.html')


def tour_register(request):
    if request.method == 'POST':
        print(request)

class TourRegisterView(CreateView):
    model = TourRegistration
    form_class = TourRegisterForm
    template_name = 'tour_register.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        tour_id = self.kwargs.get('pk')  
        return get_object_or_404(Tour, id=tour_id)

    def form_valid(self, form):
        tour = self.get_object()
        form.instance.tour = tour
        return super().form_valid(form)

