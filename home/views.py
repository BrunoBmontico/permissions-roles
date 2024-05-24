from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.permissions import revoke_permission, grant_permission
from rolepermissions.decorators import has_role_decorator, has_permission_decorator

@has_permission_decorator('ver_metas')
def home(request):

    # revoke_permission(request.user, 'ver_metas')
    grant_permission(request.user, 'ver_metas')
    print(get_user_roles(request.user))

    return render(request, 'home.html')

def criar_usuario(request):
    user = User.objects.create_user(
        username='caio',
        password='123'
    )
    user.save()
    assign_role(user, 'gerente')
    return HttpResponse('Usuario salvo')