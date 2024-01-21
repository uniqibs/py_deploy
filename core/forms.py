from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserCategoryPublishes,Likes,BanUserProduct,UserPhoto,UserCardInput,UserSocial
from django.forms import ModelForm
from django import forms


class UserSocailForm(ModelForm):
    class Meta:
        model = UserSocial
        fields = ['name', 'type_social_media']


class UserCardForm(ModelForm):
    class Meta:
        model = UserCardInput
        fields = ['card', 'type_card']
        exclude = ('user',)



class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = '__all__'
        exclude = ('user',)

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio', 'location'] 


class UserRegisTrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']



class UserBanForm(ModelForm):
    class Meta:
        model = BanUserProduct
        fields = ['ban']



class UserCategoryPublishForm(forms.ModelForm):
    class Meta:
        model = UserCategoryPublishes
        exclude = ('user', )
        

class SearchForm(forms.Form):
    name = forms.CharField(max_length=50, label='Search..')


class UserLikeForm(ModelForm):
    class Meta:
        model = Likes
        fields = ['like']


class PostDeleteForm(forms.Form):
    post_id = forms.IntegerField(widget=forms.HiddenInput)

class DeleteUserCategoryPublishesForm(forms.Form):
    buccati_value = forms.CharField(label='Значение для удаления')


class UserCategoryPublsihesSelectionForm(forms.Form):
    user_category_publsihes = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        label='Выберите объявлению для удаление '

    )

    def __init__(self, user, *args, **kwargs):
        super(UserCategoryPublsihesSelectionForm, self).__init__(*args, **kwargs)
        self.fields['user_category_publsihes'].queryset = UserCategoryPublishes.objects.filter(user=user)




class PhotoDeleteForm(forms.ModelForm):
    delete = forms.ModelMultipleChoiceField(
        queryset=None,
        widget = forms.CheckboxSelectMultiple,
        label = 'Delete photo'
    )


    def __init__(self,user,*args, **kwargs):
        super[PhotoDeleteForm,self].__init__(self,*args, **kwargs)
        self.fields['user_photo'].queryset = UserPhoto.objects.filter(user=user)