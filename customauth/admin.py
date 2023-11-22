from functools import update_wrapper
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import login
from django.contrib.contenttypes import views as contenttype_views
from django.urls import include, path, re_path
from django.contrib.auth.views import LoginView
from .models import User 

class MyAdminSite(AdminSite):
    def has_permission(self):
        return self.user.is_active and self.user.is_superuser

    def get_urls(self):

        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)

            wrapper.admin_site = self
            return update_wrapper(wrapper, view)

        urlpatterns = [
            path("", wrap(self.index), name="index"),
            path("login/", self.login, name="login"),
            path("verify/", self.verify, name="verify"),
            path("logout/", wrap(self.logout), name="logout"),
            path(
                "r/<int:content_type_id>/<path:object_id>/",
                wrap(contenttype_views.shortcut),
                name="view_on_site",
            ),
        ]


    def login(self, request):
        if request.method == "GET" and self.has_permission(request):
            index_path = reverse("admin:index", current_app=self.name)
            return HttpResponseRedirect(index_path)

        if request.method == 'POST':
            context = {}
            context['form'] = GenerateForm(request.POST)

            if context['form'].is_valid():
                return HttpResponseRedirect(reverse('admin:verify', current_app=self.name, kwargs={'user':context.form.cleaned_data['user']}))
        defaults = {
            "authentication_form": GenerateForm,
            "template_name": "admin/login.html",
        }
        request.current_app = self.name
        return LoginView.as_view(**defaults)(request)
            

    def verify(self, request):
        if request.method == "GET" and self.has_permission(request):
            index_path = reverse("admin:index", current_app=self.name)
            return HttpResponseRedirect(index_path)

        if request.method == 'GET':
            context = {}
            context['form'] = VerifyForm(request.POST)

            if context['form'].is_valid():
                return HttpResponseRedirect(reverse('admin:index', current_app=self.name, kwargs={'user':context.form.cleaned_data['user']}))
        defaults = {
            "authentication_form": VerifyForm,
            "template_name": "admin/login.html",
        }
        request.current_app = self.name
        return LoginView.as_view(**defaults)(request)


admin_site = MyAdminSite()
