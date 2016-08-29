from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View

from todo.extensions.decorators.login_required import login_required
from todo.models.todo import Todo


class Todos(View):

    @method_decorator(login_required)
    def get(self, request):
        return JsonResponse({
            'data': [
                todo.to_json() for todo in Todo.objects.filter(
                    user=request.user
                )
            ]
        })

    @method_decorator(login_required)
    def post(self, request):
        description = request.POST.get('description')

        if not description:
            return HttpResponse(
                status=400
            )

        todo = Todo.objects.create(
            user=request.user,
            is_done=False,
            description=description,
            created_at=datetime.now()
        )

        return JsonResponse({
            'data': todo.to_json()
        })


class TodoItem(View):

    @method_decorator(login_required)
    def put(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
        except:
            return HttpResponse(
                status=400
            )

        is_done = request.POST.get('is_done')

        if is_done:
            todo.is_done = is_done

        description = request.POST.get('description')

        if description:
            todo.description = description

        todo.save()

        return JsonResponse({
            'data': todo.to_json()
        })

    @method_decorator(login_required)
    def delete(self, request, id):
        try:
            Todo.objects.get(id=id).delete()
        except:
            return HttpResponse(
                status=400
            )

        return HttpResponse(
            status=200
        )
