from django.shortcuts import render, redirect

from crud.form import Contact_form
from crud.models import contact


# Create your views here.
def createcontact(request):
    form = Contact_form()
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {'form':form}
        return render(request, 'Contact.html', context)

def updatecontact(request, pk):
    Contact = contact.objects.get(id=pk)
    form = Contact_form(instance=contact)
    if request.method == 'POST':
        form = Contact_form(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {'form':form}
        return render(request, 'Contact.html', context)


def deleteContact(request, pk):
    Contact = contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('/')

    context = {'contact.id': contact}
    return render(request, 'Contact.html', context)

