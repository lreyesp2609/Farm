from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class PreventBackToLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        login_url = reverse('app:login_page')
        if request.path.rstrip('/') == login_url.rstrip('/') and request.user.is_authenticated:
            return redirect('app:dashboard')
