from accounts.forms import *
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView,ListView
from jobsapp.decorators import user_is_User
from jobsapp.models import Job
from accounts.forms import UserProfileUpdateForm



class EditProfileView(UpdateView):
    model = User
    form_class = UserProfileUpdateForm
    context_object_name = 'user'
    template_name = 'jobs/user/edit-profile.html'
    success_url = reverse_lazy('accounts:user-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_User)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

class NgoEditProfileView(UpdateView):
    model = User
    form_class = NgoProfileUpdateForm
    context_object_name = 'user'
    template_name = 'jobs/ngo/edit-profile.html'
    success_url = reverse_lazy('accounts:ngo-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    # @method_decorator(user_is_User)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj