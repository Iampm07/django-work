from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name="polls"

urlpatterns = [
    path('add_question/',views.add_question,name ='add_question'),
    path("",views.index,name="index"),
    path("detail/<int:pk>/",views.detail,name="detail"),
    path("<int:question_id>/results/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

