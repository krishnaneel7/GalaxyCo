from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import CustomerRequest

from .forms import CustomerRequestForm


# =========================================================
# CUSTOMER LOGIN
# =========================================================

def customer_login(request):

    if request.user.is_authenticated:

        if request.user.is_staff:

            return redirect("owner_dashboard")

        return redirect("customer_request")


    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            if user.is_staff:

                messages.error(
                    request,
                    "Please use the Owner Login page."
                )

                return redirect("customer_login")


            login(
                request,
                user
            )

            return redirect("customer_request")


        messages.error(
            request,
            "Invalid username or password."
        )


    return render(
        request,
        "customer_login.html"
    )


# =========================================================
# CUSTOMER REGISTER
# =========================================================

def customer_register(request):

    if request.user.is_authenticated:

        if request.user.is_staff:

            return redirect("owner_dashboard")

        return redirect("customer_request")


    if request.method == "POST":

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password")

        confirm_password = request.POST.get(
            "confirm_password"
        )


        if not username or not email or not password or not confirm_password:

            messages.error(
                request,
                "Please fill all fields."
            )

            return redirect("customer_register")


        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect("customer_register")


        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("customer_register")


        if User.objects.filter(
            email=email
        ).exists():

            messages.error(
                request,
                "Email address is already registered."
            )

            return redirect("customer_register")


        User.objects.create_user(

            username=username,

            email=email,

            password=password

        )


        messages.success(
            request,
            "Account created successfully. Please login."
        )


        return redirect(
            "customer_login"
        )


    return render(
        request,
        "customer_register.html"
    )


# =========================================================
# CUSTOMER LOGOUT
# =========================================================

def customer_logout(request):

    logout(request)

    return redirect(
        "customer_login"
    )


# =========================================================
# CUSTOMER REQUEST
# =========================================================

@login_required(login_url="/")
def customer_request(request):

    if request.user.is_staff:

        return redirect(
            "owner_dashboard"
        )


    if request.method == "POST":

        form = CustomerRequestForm(
            request.POST
        )


        if form.is_valid():

            customer_request_data = form.save(
                commit=False
            )


            customer_request_data.name = (
                request.user.username
            )


            customer_request_data.email = (
                request.user.email
            )


            customer_request_data.save()


            return redirect(
                "request_success"
            )


    else:

        form = CustomerRequestForm(

            initial={

                "name":
                request.user.username,

                "email":
                request.user.email,

            }

        )


    return render(

        request,

        "customer_request.html",

        {
            "form": form
        }

    )


# =========================================================
# REQUEST SUCCESS
# =========================================================

@login_required(login_url="/")
def request_success(request):

    if request.user.is_staff:

        return redirect(
            "owner_dashboard"
        )


    return render(
        request,
        "request_success.html"
    )


# =========================================================
# OWNER LOGIN
# =========================================================

def owner_login(request):

    if request.user.is_authenticated:

        if request.user.is_staff:

            return redirect(
                "owner_dashboard"
            )

        logout(request)

        messages.error(
            request,
            "Please login as owner."
        )


    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )


        user = authenticate(

            request,

            username=username,

            password=password

        )


        if user is not None:

            if user.is_staff:

                login(
                    request,
                    user
                )

                return redirect(
                    "owner_dashboard"
                )


            messages.error(
                request,
                "This account is not an owner account."
            )


        else:

            messages.error(
                request,
                "Invalid owner username or password."
            )


    return render(
        request,
        "owner_login.html"
    )


# =========================================================
# OWNER LOGOUT
# =========================================================

def owner_logout(request):

    logout(request)

    return redirect(
        "owner_login"
    )


# =========================================================
# OWNER DASHBOARD
# =========================================================

@login_required(login_url="/owner-login/")
def owner_dashboard(request):

    if not request.user.is_staff:

        messages.error(
            request,
            "Owner access required."
        )

        logout(request)

        return redirect(
            "owner_login"
        )


    requests = CustomerRequest.objects.all().order_by(
        "-created_at"
    )


    total_requests = (
        CustomerRequest.objects.count()
    )


    pending_requests = (
        CustomerRequest.objects.filter(
            status="Pending"
        ).count()
    )


    contacted_requests = (
        CustomerRequest.objects.filter(
            status="Contacted"
        ).count()
    )


    completed_requests = (
        CustomerRequest.objects.filter(
            status="Completed"
        ).count()
    )


    context = {

        "requests": requests,

        "total_requests": total_requests,

        "pending_requests": pending_requests,

        "contacted_requests": contacted_requests,

        "completed_requests": completed_requests,

    }


    return render(

        request,

        "owner_dashboard.html",

        context

    )


# =========================================================
# UPDATE REQUEST
# =========================================================

@login_required(login_url="/owner-login/")
def update_request(request, request_id):

    if not request.user.is_staff:

        messages.error(
            request,
            "Owner access required."
        )

        return redirect(
            "owner_login"
        )


    customer_request_data = get_object_or_404(

        CustomerRequest,

        id=request_id

    )


    if request.method == "POST":

        status = request.POST.get(
            "status"
        )


        if status in [
            "Pending",
            "Contacted",
            "Completed"
        ]:

            customer_request_data.status = status

            customer_request_data.save()


            messages.success(
                request,
                "Request status updated successfully."
            )


        return redirect(
            "owner_dashboard"
        )


    return render(

        request,

        "update_request.html",

        {
            "customer_request":
            customer_request_data
        }

    )


# =========================================================
# DELETE REQUEST
# =========================================================

@login_required(login_url="/owner-login/")
def delete_request(request, request_id):

    if not request.user.is_staff:

        messages.error(
            request,
            "Owner access required."
        )

        return redirect(
            "owner_login"
        )


    customer_request_data = get_object_or_404(

        CustomerRequest,

        id=request_id

    )


    if request.method == "POST":

        customer_request_data.delete()


        messages.success(
            request,
            "Customer request deleted successfully."
        )


    return redirect(
        "owner_dashboard"
    )