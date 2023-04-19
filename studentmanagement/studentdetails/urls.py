from django.urls import path
from .views import*
urlpatterns = [
    path('studentdetailmarks/',studentdatavalidation),
    path('studentdetailsdisplay/',studentdetaildisplay),

]
