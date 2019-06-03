from django.urls import path
from deal_app.properties.views import (
    property_list_view,
    property_detail_view,
    property_update_view,
    property_delete_view,
    property_income_update_view,
    property_purchase_update_view
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
        "<int:pk>/update/",
        view=property_update_view,
        name="update-basic"
    ),
    path(
        "<int:pk>/update-income/",
        view=property_income_update_view,
        name="update-income"
    ),
    path(
        "<int:pk>/edit-purchase/",
        view=property_purchase_update_view,
        name="edit-purchase"
    ),
    path(
        "<int:pk>/delete/",
        view=property_delete_view,
        name="delete"
    )
]
