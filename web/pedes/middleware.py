from accounts.models import ActivityLog
from django.utils import timezone


class ViewCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('HTTP_X_REAL_IP')
        if ip:  # Check if IP is available
            prev_values = ActivityLog.objects.filter(ip=ip)
            if not prev_values.exists():
                ActivityLog.objects.create(ip=ip, timestamp=timezone.now())
        # No need to create an ActivityLog object if IP is missing

        response = self.get_response(request)
        return response