from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "message/dashboard.html")

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
    # Verifica se o objeto NÂO tem o atributo
    if not hasattr(request.user, "profile"):
        missing_profile = Profile(usuario=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.seguidores.add(profile)
        elif action == "unfollow":
            current_user_profile.seguidores.remove(profile)
        current_user_profile.save()

    return render(
        request,
        "message/profile.html",
        {
            "profile": profile,
        }
    )