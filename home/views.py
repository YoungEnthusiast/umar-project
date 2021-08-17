from django.shortcuts import render, reverse, redirect
from .forms import ContactForm
from audios.models import Audio
from videos.models import Video
from news.models import News
from django.core.mail import send_mail
#from django.template.loader import render_to_string

def showHome(request):
    audios_home = Audio.objects.filter(home_page=True)
    videos_home = Video.objects.filter(home_page=True)
    news_home = News.objects.filter(home_page=True)
    context = {'audios_home': audios_home, 'videos_home': videos_home, 'news_home': news_home}
    return render(request, 'home/home.html', context)

def showAdmission(request):
    return render(request, 'home/admission.html')

def showAbout(request):
    return render(request, 'home/about.html')

def showContact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            send_mail(
                'Contact Umar bn l Khattob',
                'A message was sent by ' + name + '. Please log in to admin panel to read message',
                'yustaoab@gmail.com',
                [email],
                fail_silently=False,
                #html_message = render_to_string('home/home1.html')
            )
            messages.success(request, str(name) + ", your message will receive attention shortly")
        else:
            return redirect('contact')
    return render(request, 'home/contact_form.html', {'form': form})
