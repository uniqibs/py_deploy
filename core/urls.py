from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import UserLoginView,UserLogoutView


urlpatterns = [
    path('product_search/',views.search, name='product_search'),
    path('login/',views.login_view, name='login'),
    path('regis/',views.regis_view, name='regis'),
    path('',views.home, name='home'),
    path('logout/',views.logout_view, name='logout'),
    path('user_publish/',views.profile_publish_view, name='user_publish'),
    path('publish_succses/',views.publish_succses, name='publish_succses'),
    path('like/',views.like_view, name='like'),
    # path('proflie/<int:user_id>/',views.user_profile, name='user_profile'),
    path('product/<int:user_id>/', views.product_id_details, name='product_id_details'),
    path('ban/',views.ban_view, name='ban'),
    path('user_objetcs/', views.user_detail_with_conptent, name='user_profile'),
    path('deleted/',views.delete_selected_user_category_publsihes, name='del'),
    path('user_photo/',views.user_photo, name='user_photo'),
    path('otzif/',views.otzif, name='otzif'),
    # path('user_card/',views.user_card_input_view, name='card_input'),
    path('user_social/',views.user_social_view, name='social'),
    path('user_deteails/<int:user_id>/',views.user_details, name='details'),
    path('photo_deleted/',views.photo_deleted, name='photo_del'),
    path('card',views.card_view, name='card_input')
    



]
