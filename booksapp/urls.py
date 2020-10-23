from django.urls import path
from . import views
from books import settings
from django.views.generic import RedirectView
from django.conf.urls import url
from django.conf.urls.static import static
app_name =  "booksapp"

urlpatterns = [
    url('favicon.ico',RedirectView.as_view(url='/static/booksapp/favicon.ico')),

    path('',views.home),
    path('name/',views.name),
    path('author/',views.author),
    path('topic/',views.topic),
    path('ages/',views.ages),
    path('<slug_detail>',views.app_detail,name="detail"),
    path('author/<slug_author>',views.author_detail,name="detail_author"),
    path('topic/<slug_topic>',views.topic_detail,name="detail_topic"),
    path('ages/<slug_ages>',views.ages_detail,name="detail_ages"),
    
]+ static(settings.UPLOADED_URL, document_root=settings.UPLOADED_FOLDER)
