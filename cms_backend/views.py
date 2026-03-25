from django.http import JsonResponse


def home(request):
    return JsonResponse(
        {
            "message": "CMS Backend is running 🚀",
        }
    )
