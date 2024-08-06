from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services/services.html')

def service_sap(request):
    return render(request, 'pages/services/service_sap.html')

def products(request):
    return render(request, 'pages/products/products.html')

def digital_sign(request):
    return render(request, 'pages/products/digital_sign.html')

def case_studies(request):
    return render(request, 'pages/case_study/case_studies.html')

def case_study_1(request):
    return render(request, 'pages/case_study/case_study_1.html')

def contact(request):
    return render(request, 'pages/contact.html')

def faq(request):
    return render(request, 'pages/faq.html')

def page_not_found(request):
    return render(request, 'includes/404.html')