from django.http import HttpResponse
from django.views import View


class HomePageView(View):
    # GET request

    def get(self, request):
        return HttpResponse("Welcome to the homepage!")


# def home_page_view(request):
#  return HttpResponse("Welcome to Entity homepage!")


# def about_page_view(request):
# return HttpResponse("Entity about page!")
