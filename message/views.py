from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "base.html")

def profile_list(request):
    profiles = Profile.objects.exclude(usuario=request.user)
    return render(
        request,
        "message/profile_list.html",
        {
            "profiles": profiles,
        }
    )

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(
        request,
        "message/profile.html",
        {
            "profile": profile,
        }
    )