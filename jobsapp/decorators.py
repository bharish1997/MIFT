from django.core.exceptions import PermissionDenied


def user_is_Ngo(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'ngo':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_User(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'user':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
