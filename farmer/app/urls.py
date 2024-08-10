from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

app_name='app'

urlpatterns = [
    path('',views.login_view,name='login_page'),
    path('signup/',views.signup_view,name='signup'),
    path('register/',views.register_view,name='register'),
    path('dashboard/',views.dashboard_view,name='dashboard'),

    path('farms/', views.farm_list, name='farm_list'),
    path('farms/<int:farm_id>/', views.view_farm, name='view_farm'),
    path('farms/add/', views.add_farm, name='add_farm'),
    path('farms/edit/<int:farm_id>/', views.edit_farm, name='edit_farm'),
    path('farms/delete/<int:farm_id>/', views.delete_farm, name='delete_farm'),

    path('crops/', views.crop_list, name='crop_list'),
    path('crops/<int:crop_id>/', views.view_crop, name='view_crop'),
    path('crops/add/', views.add_crop, name='add_crop'),
    path('crops/edit/<int:crop_id>/', views.edit_crop, name='edit_crop'),
    path('crops/delete/<int:crop_id>/', views.delete_crop, name='delete_crop'),

    path('livestocks/', views.livestock_list, name='livestock_list'),
    path('livestocks/<int:livestock_id>/', views.view_livestock, name='view_livestock'),
    path('livestocks/add/', views.add_livestock, name='add_livestock'),
    path('livestocks/edit/<int:livestock_id>/', views.edit_livestock, name='edit_livestock'),
    path('livestocks/delete/<int:livestock_id>/', views.delete_livestock, name='delete_livestock'),
   
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/<int:expense_id>/', views.view_expense, name='view_expense'),
    path('expenses/edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('expenses/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),

    path('expense-summary/', views.expense_summary, name='expense_summary'),
    path('detailed-reports/', views.detailed_reports, name='detailed_reports'),
   
    path('set_budget/<int:expense_id>/', views.set_budget, name='set_budget'),
    path('financial_reports/', views.financial_reports, name='financial_reports'),

    path('add_sale/',views.add_sale, name='add_sale'),
    path('sale_list/', views.sale_list, name='sale_list'),
    path('remove_sale/<int:sale_id>/', views.remove_sale, name='remove_sale'),


    path('switch-language/<str:language>/', views.switch_language, name='switch_language'),

    path('custom_logout/', views.custom_logout, name='custom_logout'),

    path('error/', views.error, name='error'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)