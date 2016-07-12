from django.contrib import auth
from django.views.generic import View
from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest


class Login(View):

    def post(self, request):
        login = request.POST.get('login')
        password = request.POST.get('password')

        user = auth.authenticate(
            username=login,
            password=password
        )

        if not user:
            return HttpResponseBadRequest(
                status=400
            )

        auth.login(request, user)

        return JsonResponse({
            'user': user.to_json()
        })


class Logout(View):

    def post(self, request):
        auth.logout(request)

