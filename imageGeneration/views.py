from django.shortcuts import render
from .models import Prompt, Image
from django.contrib.auth.decorators import login_required


def prompt(request):
    '''Show all prompts'''
    prompt = Prompt.objects.all()
    context = {'prompt': prompt}
    return render(request, 'imageGeneration/prompt.html', context)


def image(request):
    '''Show all images'''
    image = Image.objects.all()
    context = {
        'image': image,
    }
    return render(request, 'imageGeneration/image.html', context)


def gallery(request):
    '''Show the gallery'''
    gallery = Image.objects.all()
    context = {
        'gallery': gallery,
    }
    return render(request, 'imageGeneration/gallery.html', context)