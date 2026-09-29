from django.urls import path

from . import views


urlpatterns = [

    # Customer
    path(
        "",
        views.customer_login,
        name="customer_login"
    ),

    path(
        "register/",
        views.customer_register,
        name="customer_register"
    ),

    path(
        "logout/",
        views.customer_logout,
        name="customer_logout"
    ),

    path(
        "request/",
        views.customer_request,
        name="customer_request"
    ),

    path(
        "request/success/",
        views.request_success,
        name="request_success"
    ),


    # Owner
    path(
        "owner-login/",
        views.owner_login,
        name="owner_login"
    ),

    path(
        "owner-logout/",
        views.owner_logout,
        name="owner_logout"
    ),

    path(
        "owner-dashboard/",
        views.owner_dashboard,
        name="owner_dashboard"
    ),

    path(
        "owner/request/<int:request_id>/update/",
        views.update_request,
        name="update_request"
    ),

    path(
        "owner/request/<int:request_id>/delete/",
        views.delete_request,
        name="delete_request"
    ),

]