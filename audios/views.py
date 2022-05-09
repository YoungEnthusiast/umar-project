from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Audio
from .forms import AudioForm, AudioFormUp, CategoryForm, CategoryFormUp
from .filters import AudioFilter, CategoryFilter
from django.core.paginator import Paginator
from .models import Audio
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import Category, Audio
from .filters import AudioFilter
from django.core.paginator import Paginator
from .models import Audio

def showAudios(request):
    context = {}
    audios = Audio.objects.all()
    filtered_audios = AudioFilter(
        request.GET,
        queryset = Audio.objects.all()
    )
    context['filtered_audios'] = filtered_audios
    paginated_filtered_audios = Paginator(filtered_audios.qs, 9)
    page_number = request.GET.get('page')
    audios_page_obj = paginated_filtered_audios.get_page(page_number)
    context['audios_page_obj'] = audios_page_obj
    total_audios = filtered_audios.qs.count()
    context['total_audios'] = total_audios
    return render(request, 'audios/audios.html', context=context)

@login_required
def showAudiosFirst(request, category_slug=None):
    context = {}
    audios = Audio.objects.all()
    filtered_audios = AudioFilter(
        request.GET,
        queryset = Audio.objects.all()
    )
    context['filtered_audios'] = filtered_audios
    paginated_filtered_audios = Paginator(filtered_audios.qs, 9)
    page_number = request.GET.get('page')
    audios_page_obj = paginated_filtered_audios.get_page(page_number)
    context['audios_page_obj'] = audios_page_obj
    total_audios = filtered_audios.qs.count()
    context['total_audios'] = total_audios
    return render(request, 'audios/audios_first.html', context=context)

@login_required
def showCategoriesFirst(request, category_slug=None):
    context = {}
    categories = Category.objects.all()
    filtered_categories = CategoryFilter(
        request.GET,
        queryset = Category.objects.all()
    )
    context['filtered_categories'] = filtered_categories
    paginated_filtered_categories = Paginator(filtered_categories.qs, 9)
    page_number = request.GET.get('page')
    categories_page_obj = paginated_filtered_categories.get_page(page_number)
    context['categories_page_obj'] = categories_page_obj
    total_categories = filtered_categories.qs.count()
    context['total_categories'] = total_categories
    return render(request, 'audios/categories_first.html', context=context)

@login_required
def updateAudioFirst(request, id):
    audio = Audio.objects.get(id=id)
    form = AudioFormUp(instance=audio)
    if request.method=='POST':
        form = AudioFormUp(request.POST, request.FILES, instance=audio)
        if form.is_valid():
            form.save()
            messages.success(request, "The audio has been modified successfully")
            return redirect('audios_first')
    return render(request, 'audios/audio_update_first.html', {'form': form, 'audio': audio})

@login_required
def updateCategoryFirst(request, id):
    category = Category.objects.get(id=id)
    form = CategoryFormUp(instance=category)
    if request.method=='POST':
        form = CategoryFormUp(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "The category has been modified successfully")
            return redirect('audios_categories_first')
    return render(request, 'audios/category_update_first.html', {'form': form})

@login_required
def deleteAudioFirst(request, id):
    audio = Audio.objects.get(id=id)
    obj = get_object_or_404(Audio, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('audios_first')
    return render(request, 'audios/audio_confirm_delete.html', {'audio': audio})

@login_required
def deleteCategoryFirst(request, id):
    category = Category.objects.get(id=id)
    obj = get_object_or_404(Category, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('audios_categories_first')
    return render(request, 'audios/category_confirm_delete.html', {'category': category})

@login_required
def addAudio(request):
    form = AudioForm()
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The audio has been added successfully")
            return redirect('audios_first')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'audios/audio_first.html', {'form': form})

@login_required
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "The category has been added successfully")
            return redirect('audios_categories_first')
        else:
            messages.error(request, "Please review form input fields below")
    return render(request, 'audios/category_first.html', {'form': form})
