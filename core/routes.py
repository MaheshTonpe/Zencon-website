from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name="home-page"),
    path('about/', views.about, name="about-page"),
    path('services/', views.services, name="services-page"),
    path('service-sap/', views.service_sap, name="service-sap-page"),
    path('products/', views.products, name="products-page"),
    path('digital-sign/', views.digital_sign, name="digital-sign-page"),
    path('case-studies/', views.case_studies, name="case-studies-page"),
    path('case-study-1/', views.case_study_1, name="case-study-1-page"),
    path('contact/', views.contact, name="contact-page"),
    path('faq/', views.faq, name="faq-page"),
]

urlpatterns +=[
    path('404/', views.page_not_found, name="page-not-found-page"),
]