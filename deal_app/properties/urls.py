from django.urls import path
from deal_app.properties.views import (
    property_list_view,
    property_detail_view,
    property_update_view,
    property_delete_view,
    property_income_update_view,
    property_purchase_update_view,
    property_create_view
)

app_name = "properties"
urlpatterns = [
    path(
        '<int:pk>/',
        view=property_detail_view,
        name="detail"
    ),
    path(
        '',
        view=property_list_view,
        name="list"
    ),
    path(
        "create/",
        view=property_create_view,
        name="create-property"
    ),
    path(
        "update/<int:pk>",
        view=property_update_view,
        name="update-basic-info"
    ),
    path(
        "update-income/<int:pk>/",
        view=property_income_update_view,
        name="update-income"
    ),
    path(
        "edit-purchase/<int:pk>/",
        view=property_purchase_update_view,
        name="edit-purchase"
    ),
    path(
        "<int:pk>/delete/",
        view=property_delete_view,
        name="delete"
    )
]
