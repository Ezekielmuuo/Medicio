from django.shortcuts import render, redirect
from medicioapp.models import Contact, Appointment, Branch


def index(request):
    return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def contact(request):
    return render(request, 'contact.html')


def department(request):
    return render(request, 'departments.html')


def contacts(request):
    if request.method == 'POST':
        all = Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      message=request.POST['message'],
                      )
        all.save()
        return redirect('contacts/')

    else:
        return render(request, 'contacts.html')


def appoint(request):
    if request.method == 'POST':
        myappointments = Appointment(
                            name=request.POST['name'],
                            email=request.POST['email'],
                            phone=request.POST['phone'],
                            date=request.POST['date'],
                            department=request.POST['department'],
                            doctor=request.POST['doctor'],
                            message=request.POST['message'],
                            )
        myappointments.save()
        return redirect('/appointment')

    else:
        return render(request, 'appointment.html')


def branch(request):
    if request.method == 'POST':
        apt = Branch( name=request.POST['name'],
                      location=request.POST['location'],
                      manager=request.POST['manager'],
                      email=request.POST['email'],
                      )
        apt.save()
        return redirect('/Branch')

    else:
        return render(request, 'Branch.html')
