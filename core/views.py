from django.shortcuts import (render,
                              redirect,
                              get_object_or_404,
                              )
from django.contrib.auth import (authenticate,
                                 login,
                                 logout)
from django.contrib import messages
from django.contrib.auth.decorators import (login_required)
from .models import(UserCategoryPublishes,
                    Likes,
                    UserPhoto,
                    BanUserProduct,
                    ConetntView
                    )
from .forms import (UserCategoryPublishForm,
                    UserRegisTrationForm,
                    SearchForm,
                    User,
                    UserLikeForm,
                    UserBanForm,
                    UserCategoryPublsihesSelectionForm,
                    UserPhotoForm,
                    UserCardInput,
                    UserCardForm,
                    UserSocailForm,
                    UserSocial,
                    PhotoDeleteForm)
from django.contrib.auth.views import (LogoutView,
                                        LoginView
                                    as BaseLoginVIew)

from django import views
from django.views import View
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.http import HttpResponseForbidden



"""Hello my gays my name is ibragim, I am  Backend developer my skils python, Django freamework, and Html Css"""
@login_required
def user_details(request,user_id):

    user = request.user
    user_ob  = User.objects.filter(pk=user_id)
    user_photo = UserPhoto.objects.filter(pk=user_id)
    user_like = Likes.objects.filter(pk=user_id)
    user_content = UserCategoryPublishes.objects.filter(pk=user_id)
    user_card = UserCardInput.objects.filter(pk=user_id)
    user_social = UserSocial.objects.filter(pk=user_id)
    context = {
        'user': user,
        'user_content': user_content,
        "photo":user_photo,
        "user_like":user_like,
        "user_card":user_card,
        "user_social":user_social,
    }
    return render(request, 'core/deteails.html', context)




@login_required
def user_social_view(request):
    form = UserSocailForm()
    if request.method == 'POST':
        form = UserSocailForm(request.POST)
        if form.is_valid():
            form.save()
            new_publish = form.save(commit=False)
            new_publish.user = request.user
            new_publish.save()
            return redirect('user_profile')
    
    sql_table = {
        "form":form
    }
    return render(request, 'core/user_social.html', sql_table)



@login_required
def user_card_input_view(request):
    form = UserCardForm()
    if request.method == 'POST':
        form = UserCardForm(request.POST)
        if form.is_valid():
            new_publish = form.save(commit=False)
            new_publish.user = request.user
            new_publish.save()
            return redirect('user_profile')
    table = {
        "form":form
    }
    return render(request, 'core/user_card.html', table)

@login_required
def photo_deleted(request):
    form = UserPhotoForm()
    user = request.user
    user_photo  = UserPhoto.objects.filter(user=user)
    if request.method == 'POST':
        form = UserPhotoForm(user, request.POST)
        if form.is_valid():
            selected_photo = form.cleaned_data['user_photo']
            user_photo.delete()
            return redirect('user_profile')
        else:
            form = UserPhotoForm(user=user, initial={"user_photo":user_photo})
    return render(request, 'core/photo_deleted.html', {"form":form})




@login_required
def delete_selected_user_category_publsihes(request):
    user = request.user
    user_category_publsihes = UserCategoryPublishes.objects.filter(user=user)
    if request.method == 'POST':
        form = UserCategoryPublsihesSelectionForm(user, request.POST)
        if form.is_valid():
            selected_user_category_publsihes = form.cleaned_data['user_category_publsihes']
            selected_user_category_publsihes.delete()
            return redirect('home')  
    else:
        form = UserCategoryPublsihesSelectionForm(user=user, initial={'user_category_publsihes': user_category_publsihes})
    return render(request, 'core/deleted.html', {'form': form})


@login_required
def product_id_details(request, user_id):
    user = request.user
    user = UserCategoryPublishes.objects.get(pk=user_id)
    usere = UserPhoto.objects.filter(pk=user_id)
    viewe = get_object_or_404(UserCategoryPublishes, pk=user_id)
    if  not ConetntView.objects.filter(user=request.user, content=viewe).exists():
        ConetntView.objects.create(user=request.user, content=viewe)
        viewe.viewer += 1
        viewe.save()

    form = BanUserProduct()
    if request.method == 'POST':
        form = UserBanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publish_succses')
        """"Like form """
    form = UserLikeForm()
    if request.method == 'POST':
            form = UserLikeForm(request.POST)
            if form.is_valid():
                new_publish = form.save(commit=False)
            new_publish.user = request.user
            new_publish.save()
            return redirect('home')
    return render(request, 'core/product_view.html', {'user':user, 'form':form, "were":usere , 'views':viewe })
    



@login_required
def otzif(request):
    user = BanUserProduct.objects.all().count()
    return render(request, 'core/product_view.html', {"ban":user})

class UserLoginView(BaseLoginVIew):
    template_name = 'core/login_view.html'
    success_url = 'home',
    

class UserLogoutView(LogoutView):
    next_page = 'login' 



@login_required
def like_view(request):
    form = UserLikeForm()
    like = Likes.objects.all().count()
    if request.method == 'POST':
        form = UserLikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publish_succses')
    like_table = {
        "form":form,
        "like":like
    }
    return render(request, 'core/like.html',like_table)





def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'LOGIN ERRROR')
    return render(request, 'core/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def regis_view(request):
    form = UserRegisTrationForm()
    if request.method == 'POST':
        form = UserRegisTrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    sql_table = {
        "form":form
    }
    return render(request, 'core/regis.html', sql_table)



@login_required
def home(request):
    user = UserCategoryPublishes.objects.all()
    user_liked = Likes.objects.all().count()
    return render(request, 'core/home.html', {"user":user, "likes":user_liked})

# @login_required
# def user_profile(request, user_id):
#     user = get_object_or_404(UserCategoryPublishes, pk=user_id)
#     return render(request, 'core/user_profile.html', {'user': user})



@login_required
def profile_publish_view(request):
    if request.method == 'POST':
        form = UserCategoryPublishForm(request.POST, request.FILES)
        if form.is_valid():
            new_publish = form.save(commit=False)
            new_publish.user = request.user
            new_publish.save()
            return redirect('user_profile') 
    else:
        form = UserCategoryPublishForm()
    return render(request, 'core/user_publish.html', {'form': form})

@login_required
def publish_succses(request):
    return render(request, 'core/publish_succses.html')         



# @login_required
# def user_profile(request, user_id):
#     user = get_object_or_404(UserCategoryPublishes, pk=user_id)
#     return render(request, 'core/user_profile.html', {"user":user})



@login_required
def regis_form(request):
    form = UserRegisTrationForm()
    if request.method == 'POST':
        form = UserRegisTrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    sql3_table = {
        "form":form
    }
    return render(request, 'core/regis.html', sql3_table)



@login_required
def search(request):
    form = SearchForm(request.GET or None)
    users = None
    if request.method == 'GET':
        if form.is_valid():
            search_query = form.cleaned_data.get('name')
            users = UserCategoryPublishes.objects.filter(name__icontains = search_query)
    return render(request, 'core/search.html', {"form":form, "users":users})


@login_required
def ban_view(request):
    form = UserBanForm()
    if request.method == 'POST':
        form = UserBanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publish_succses')
    sql_table = {
    
        "form":form
    }
    return render(request, 'core/ban.html', sql_table)





@login_required
def user_photo(request):
    user_profile, created = UserPhoto.objects.get_or_create(user=request.user)

    if not created and user_profile.user_photo:
       messages.success(request, '')
    if request.method == 'POST':
        form = UserPhotoForm(request.POST,  request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile') 
    else:
        form = UserPhotoForm(instance=user_profile)

    return render(request, 'core/photo.html', {'form': form})

@login_required
def user_detail_with_conptent(request):
    user = request.user 
    user_photo = UserPhoto.objects.filter(user=user)
    user_like = Likes.objects.filter(user=user)
    user_content = UserCategoryPublishes.objects.filter(user=user)
    user_card = UserCardInput.objects.filter(user=user)
    user_social = UserSocial.objects.filter(user=user)
    context = {
        'user': user,
        'user_content': user_content,
        "user_photo":user_photo,
        "user_like":user_like,
        "user_card":user_card,
        "user_social":user_social
    }
    return render(request, 'core/user_objects.html', context)


@login_required
def dele(request):
    return render(request, 'core/user_objects.html')


"""""""The end"""""""




@login_required
def console_log(request):
    user = UserCategoryPublishes.objects.all()
    return render(request, 'core/test.html', {"user":user})

@login_required
def saecrh_form(request):
    form = SearchForm(request.GET or None)
    users = None
    if request.method == 'GET':
        if form.is_valid():
            search_query = form.cleaned_data.get('name')
            users = UserCategoryPublishes.objects.filter(name__iconatains = search_query)
    return render(request, 'core/search.html', {'form':form, 'users':users})


def regis_view(request):
    form = UserRegisTrationForm()
    if request.method == 'POST':
        form = UserRegisTrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    slq3_table = {
        "form":form
    }
    return render(request, 'core/regis.html', slq3_table)

def login_id(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'LOGIN SUCCSES')
            return redirect('home')
        else:
            messages.error(request, 'LOGIN ERROR')
    return render(request, 'core/login.html')

"""""""OR LoginBaseView"""""""
class LoginView(BaseLoginVIew):
    template_name = 'core/login.html'
    success_url = 'home'

        
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def product_user_view(request, product_id):
    product = UserCategoryPublishes.objects.get_or_create(UserCategoryPublishes, pk=product_id)
    return render(request, 'core/product_view.html', {"product":product})






@login_required
def card_view(request):
    form = UserCardForm()
    user_profile , created = UserCardInput.objects.get_or_create(user=request.user)
    if not created and user_profile.card:
        messages.error(request, '')
    if request.method == 'POST':
            form = UserCardForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('user_profile')
    else:
            form = UserCardForm(instance=user_profile)
    return render(request, 'core/user_card.html', {"form":form})


