from django.shortcuts import render, redirect
from .models import Skin
from django.template import loader
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives, send_mail


# call index the main page
# /skins -> index (map url)
def home(request):
    return render(request, 'home.html')


def index(request):
    skins = Skin.objects.all()
    return render(request, 'index.html', {'skins': skins})


def gmail(request):
    return render(request, 'gmail.html')


def send(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    template = loader.get_template('contact_form')
    context = {
        'name': name, 'email': email,
        'subject': subject, 'message': message
    }
    message = template.render(context)

    send_mail(
        "CS_WEBSITE (message)",  # subject
        "",  # message in plain text
        "New messages" + "- Customers",  # from email
        [email],  # list of recipient emails
        html_message=message,  # message in HTML format
    )
    messages.success(request, 'Your message has been sent successfully!')
    return redirect('home')


def search_skins(request):
    if request.method == "POST":
        searched = request.POST['searched']
        skins = Skin.objects.filter(name__contains=searched)
        return render(request, 'search_skins.html', {'searched': searched,
                                                     'skins': skins})
    else:
        return render(request, 'search_skins.html', {})
