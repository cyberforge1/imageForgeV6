from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Imports for the django view function executions
from django.http import HttpResponse
import subprocess






def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

# Addition of imageForge Views

def generation(request):
    """Show generation page."""
    return render(request, 'learning_logs/generation.html')

def gallery(request):
    """Show gallery page."""
    return render(request, 'learning_logs/gallery.html')

def user_history(request):
    """Show user history page."""
    return render(request, 'learning_logs/user_history.html')

def about(request):
    """Show the about page."""
    return render(request, 'learning_logs/about.html')


# Button function executions

def execute_prompt_file(request):
    try:
        subprocess.run(["python", "newPromptInstance.py"], check=True)
    except subprocess.CalledProcessError:
        # Handle any errors that occurred during execution
        return HttpResponse("Error executing the file")

    return HttpResponse("File executed successfully")


def execute_image_file(request):
    try:
        subprocess.run(["python", "newImageInstance.py"], check=True)
    except subprocess.CalledProcessError:
        # Handle any errors that occurred during execution
        return HttpResponse("Error executing the file")

    return HttpResponse("File executed successfully")
