from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from .models import Resume
from .forms import ResumeForm
import os

# Create your views here.

def index(request):
    return render(request, 'portfolio_website/index.html')

def portfolio(request):
    resume = Resume.objects.last()
    form = ResumeForm()

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')

    context = {'resume': resume, 'form': form}
    return render(request, 'portfolio_website/resume.html', context)

def download_resume(request):
    resume = Resume.objects.last()
    if not resume:
        raise Http404("Resume not found.")
    file_path = resume.file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)