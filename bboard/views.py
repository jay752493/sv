from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView 

from .models import Bb, Rubric
from .forms import BbForm, AIFormSet, AdditionalImageForm

# Create your views here.
def index(request):
    bbs = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs, 'rubrics': rubrics})

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id = rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILES)
        if form.is_valid():
            bb = form.save()
            formset = AIFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS,'Лицо добавлено')
                return redirect('index')
    else:
        form = BbForm()
        formset = AIFormSet()
    context = {'form': form, 'formset': formset}
    return render(request, 'bboard/create.html', context)

def detail(request, rubric_pk, pk):
    bb = get_object_or_404(Bb, pk=pk)
    ais = bb.additionalimage_set.all()
    rubrics = Rubric.objects.all()
    context = {'bb': bb, 'ais': ais, 'rubrics': rubrics}
    return render(request, 'bboard/detail.html', context)

@login_required
def edit(request,rubric_pk, pk):
    bb = get_object_or_404(Bb, pk=pk)
    if request.method == 'POST':
        form = BbForm(request.POST, request.FILES, instance=bb)
        if form.is_valid():
            bb = form.save()
            formset = AIFormSet(request.POST, request.FILES, instance=bb)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS,'Лицо изменено')
                return redirect('detail', rubric_pk=rubric_pk, pk=pk)
    else:
        form = BbForm(instance=bb)
        formset = AIFormSet(instance=bb)
    context = {'form': form, 'formset': formset}
    return render(request, 'bboard/edit.html', context)


class BBLoginView(LoginView): 
    template_name = 'bboard/login.html'
 
