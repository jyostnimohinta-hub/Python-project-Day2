from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("admin_dashboard")

        messages.error(request, "Invalid admin credentials")

    return render(request, "shop/admin/admin_login.html")


def admin_check(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(admin_check, login_url="admin_login")
def admin_dashboard(request):

    return render(
        request,
        "shop/admin/dashboard.html"
    )


def admin_logout(request):
    logout(request)
    return redirect("admin_login")