from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Client
from .forms import ClientForm

# Create your views here.
# Functional based view
# Create a Client
# def Client_create(request):
#     if request.method == "POST":
#         form = ClientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("Clients:Client_list"))
#     else:
#         form = ClientForm()
#
#     return render(request, "Clients/Client_form.html", { "form": form, })
#
#
# # Retrieve Client list
# def Client_list(request):
#     Clients = Client.objects.all()
#     return render(request, "Clients/Client_list.html", { "Clients": Clients,})
#
#
# # Retrieve a single Client
# def Client_detail(request, pk):
#     Client = get_object_or_404(Client, pk=pk)
#     return render(request, "Clients/Client_detail.html", { "Client": Client, })
#
#
# # Update a single Client
# def Client_update(request, pk):
#     Client_obj = get_object_or_404(Client, pk=pk)
#     if request.method == 'POST':
#         form = ClientForm(instance=Client_obj, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("Clients:Client_detail", args=[pk,]))
#     else:
#         form = ClientForm(instance=Client_obj)
#
#     return render(request, "Clients/Client_form.html", { "form": form, "object": Client_obj})
#
#
# # Delete a single Client
# def Client_delete(request, pk):
#     Client_obj = get_object_or_404(Client, pk=pk)
#     Client_obj.delete()
#     return redirect(reverse("Clients:Client_list"))

# Class Based Views
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('clients:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:client_list')
