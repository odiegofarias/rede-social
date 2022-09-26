from django.shortcuts import render, redirect
from .models import Profile, Mensagem
from .forms import MessageForm


def dashboard(request):
    # preenche o form com os dados que chegaram do request.POST
    form = MessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.user = request.user
            mensagem.save()

            return redirect("message:dashboard")

    followed_messages = Mensagem.objects.filter(
        user__profile__in=request.user.profile.seguidores.all()
    ).order_by('-created_at')
    return render(
        request,
        "message/dashboard.html",
        {
            "form": form,
            "mensagens": followed_messages,
        }
    )

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