"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import math
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def rectangle_area(request):
    try:
        width = int(request.GET.get("width"))
        height = int(request.GET.get("height"))
        area = width * height
        response = HttpResponse(f"<h3>The area of your rectangle is {area}</h3>")
        return response
    except:
        response = HttpResponse()
        response.status_code = 418
        return response

def rectangle_perimeter(request, width, height):
    perimeter = 2 *(width + height)
    response = HttpResponse(f"<h3>The perimeter of your rectangle is {perimeter}</h3>")
    return response

def circle_area(request, radius):
    radius = int(math.pi * (radius ** 2))
    response = HttpResponse (f"<h3>The area of your circle is {radius}</h3>")
    return response

def circle_perimeter(request, radius):
    perimeter = round((2 * math.pi * radius), 2)
    response = HttpResponse (f"<h3>The perimeter of your circle is {perimeter}</h3>")
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area', rectangle_area),
    path('rectangle/perimeter/<int:width>/<int:height>', rectangle_perimeter),
    path('circle/area/<int:radius>', circle_area),
    path('circle/perimeter/<int:radius>', circle_perimeter),
]
