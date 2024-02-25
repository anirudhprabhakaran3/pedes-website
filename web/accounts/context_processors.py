from accounts.models import ActivityLog


def view_count_processor(request):
    count = ActivityLog.objects.all().count()

    return {"view_count": count}
