from django.urls import path

from .views import HomeView, MessageDetailView, AddEmailView, welcome_page, AcademicListView

urlpatterns = [
    path('', welcome_page, name="welcome_page"),
    path('home', HomeView.as_view(), name="home"),
    path('details/<int:pk>', MessageDetailView.as_view(), name="message-details"),
    path('send_message/', AddEmailView.as_view(), name='send_message'),
    #path('academic/<str:aca>/', academic_category_detail, name='academic'),
    #path('academic/academic-category', academic_category,name='academic'),
    path('academic/<slug:aca>', AcademicListView.as_view(), name='academic_category_detail'),
    path('academic/', AcademicListView.as_view(), name='academic_category'),
]
