from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from tablib import Dataset

from django.contrib.auth.forms import UserCreationForm
from Account.forms import RegistrationForm
from Account.models import Users
from .resources import *
from .models import *
from .filters import *

# ------------------ routes --------------- #

def register_view(request):
    logout_user(request)
    context={}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(email=email, password=raw_password)
            #messages.info(request, 'User account is created')
            return redirect('login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Email or Password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect("home")

def home_view(request):
    saleData = Sales.objects.all()
    context={'lists' : saleData}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def dashboard_view(request):
    context = {}
    return render(request, "Main/dashboard.html", context)


# ----------------- tables ---------------- #

@login_required(login_url='login')
def ar_table_view(request):
    artable_list = AR.objects.all()
    myfilter = arFilter(request.GET, queryset=artable_list)
    artable_list = myfilter.qs
    context = {'artable': artable_list, 'myfilter':myfilter}

    if request.method == 'POST':
        ar_resource = AR_resource()
        dataset = Dataset()
        new_ar = request.FILES['input_data']
        imported_data = dataset.load(
            new_ar.read().decode('utf-8'), format='csv')
        result = ar_resource.import_data(dataset, dry_run=True)

        if result.has_validation_errors() or result.has_errors():
            return JsonResponse({'message': 'validation error'}, status=500)
        else:
            ar_resource.import_data(dataset, dry_run=False)
            return JsonResponse({'message': 'File uploaded successfully'}, status=200)
    return render(request, "Main/artable.html", context)


@login_required(login_url='login')
def parties_table_view(request):
    partie_list = Parties.objects.all()
    myfilter = partieFilter(request.GET, queryset=partie_list)
    partie_list = myfilter.qs
    context = {'partiestable': partie_list, 'myFilter':myfilter}

    if request.method == 'POST':
        partie_resource = Parties_resource()
        dataset = Dataset()
        new_partie = request.FILES['input_data']
        imported_data = dataset.load(
            new_partie.read().decode('utf-8'), format='csv')
        result = partie_resource.import_data(dataset, dry_run=True)

        if result.has_validation_errors() or result.has_errors():
            return JsonResponse({'message': 'validation error'}, status=500)
        else:
            partie_resource.import_data(dataset, dry_run=False)
            return JsonResponse({'message': 'File uploaded successfully'}, status=200)
    return render(request, "Main/partiestable.html", context)


@login_required(login_url='login')
def purchase_table_view(request):
    purchase_list = Purchases.objects.all()
    myfilter = purchaseFilter(request.GET, queryset=purchase_list)
    purchase_list = myfilter.qs
    context = {'purchasetable': purchase_list, 'myFilter':myfilter}

    if request.method == 'POST':
        purchase_resource = Purchase_resource()
        dataset = Dataset()
        new_purchase = request.FILES['input_data']
        imported_data = dataset.load(
            new_purchase.read().decode('utf-8'), format='csv')
        result = purchase_resource.import_data(dataset, dry_run=True)

        if result.has_validation_errors() or result.has_errors():
            return JsonResponse({'message': 'validatiion error'}, status=500)
        else:
            purchase_resource.import_data(dataset, dry_run=False)
            return JsonResponse({'message': 'File uploaded successfully'}, status=200)
    return render(request, "Main/purchasetable.html", context)


@login_required(login_url='login')
def sale_table_view(request):
    sales_list = Sales.objects.all()
    myfilter = saleFilter(request.GET, queryset=sales_list)
    sales_list = myfilter.qs
    context = {'saletable': sales_list, 'myfilter':myfilter}

    if request.method == 'POST':
        sale_resource = Sale_resource()
        dataset = Dataset()
        new_sale = request.FILES['input_data']
        imported_data = dataset.load(
            new_sale.read().decode('utf-8'), format='csv')
        result = sale_resource.import_data(dataset, dry_run=True)

        if result.has_validation_errors() or result.has_errors():
            return JsonResponse({'message': 'validation error'}, status=500)
        else:
            sale_resource.import_data(dataset, dry_run=False)
            return JsonResponse({'message': 'File uploaded successfully'}, status=200)
    return render(request, "Main/saletable.html", context)