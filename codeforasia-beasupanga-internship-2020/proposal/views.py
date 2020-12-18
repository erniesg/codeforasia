from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProjectProposalForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Proposal
from django.contrib import messages

@login_required
def index(request):
    form = ProjectProposalForm()
    proposals = Proposal.objects.all
    if request.method == 'POST':
        form = ProjectProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proposal_index")
        else: 
            messages.error(request, "Oops! There was an error saving the proposal. Please try again.", extra_tags='alert-danger')
            return redirect("proposal_index")
    context = {
        'proposals': proposals,
        'form': form
    }
    return render(request, 'proposal/index.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("proposal_index")
        else: 
            messages.error(request, "Oops! This user doesn't exists.", extra_tags='alert-danger')
            return redirect("proposal_index")
    context = {}
    return render(request, 'proposal/login.html', context)

def registerPage(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            User = authenticate(
                username=username,
                password=password
            )
            login(request, User)
            return redirect('proposal_index')
        else:
            form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'proposal/register.html', context)

@login_required
def logoutPage(request):
    logout(request)
    return redirect('proposal_index')
