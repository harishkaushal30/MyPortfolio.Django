from django.shortcuts import render
from blog.models import Post
from .forms import ContactForm
from .models import Contact
import os
from django.contrib import messages

def index(request):
    myinfo = myInfo()
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            new_message = Contact(
                name = data['name'],
                email_id = data['email_id'],
                subject = data['subject'],
                message = data['message']
            )
            new_message.save()
            messages.success(request, "Message Sent !!")
    posts = Post.objects.filter(state='PUBLISHED').order_by('-created_on')
    context = {
        'aboutMe': myinfo.aboutMe,
        'skills': myinfo.skills,
        'posts': posts,
        'contact_form': contact_form,
    }
    return render(request, "index.html", context)

def error(request):
    return render(request, "error.html")

class myInfo:
    aboutMe = "Experienced Service Engineer with a demonstrated history of working in the computer software industry. Strong engineering professional with a Bachelor of Technology (B.Tech.) focused in Computer Science from KC College of Engineering and IT. Currently pursing Part time MS from IIIT, Hyderbad."
    skills = {'Automation': 80, 'Windows Infra': 85, 'Backend developer': 75, 'OOPS': 70, 'PowerShell': 90}
    certs = []

    # def get_certs(self):
    #     path = "certs/"
    #     files = os.listdir(path)
    #     for file in files:
    #         self.certs.append(file)