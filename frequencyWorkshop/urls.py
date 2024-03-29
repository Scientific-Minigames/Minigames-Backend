from django.urls import path

from frequencyWorkshop.views import soundFilter, fftView, timeView

app_name='frequencyWorkshop'
urlpatterns = [
    path('fft/', fftView, name='fft'),
    path('timeplot/', timeView, name='timeplot'),
    path('filter/', soundFilter, name='filter')
]   
