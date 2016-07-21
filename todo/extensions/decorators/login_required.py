from django.http import HttpResponse


def login_required(function=None):
    def _decorator(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponse(status=401)

        return function(request, *args, **kwargs)

    return _decorator
