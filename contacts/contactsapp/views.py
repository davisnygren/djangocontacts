from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django import forms
from django.utils import timezone

from .models import Contact

import datetime

class AddContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name']


class IndexView(generic.ListView):
    template_name = 'contactsapp/index.html'
    context_object_name = 'all_contact_list'

    def get_queryset(self):
        """Return all added contacts."""
        return Contact.objects.all()


class DetailView(generic.DetailView):
    model = Contact
    template_name = 'contactsapp/detail.html'


class AddContactView(generic.FormView):
    template_name = 'contactsapp/add_contact.html'
    form_class = AddContactForm
    success_url = '/contactsapp/'

    def form_valid(self, form):
        return super(AddContactView, self).form_valid(form)


def postContact(request):
    try:
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
    except (KeyError, Contact.DoesNotExist):
        return render(request, 'contactsapp/add_contact.html', {
            'error_message': "You enter all information correctly.",
        })
    else:
        contact = Contact.create(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, add_date=timezone.now())
        contact.save()
        # selected_choice.votes += 1
        # selected_choice.save()
        return HttpResponseRedirect(reverse('contactsapp:detail', args=(contact.pk,)))