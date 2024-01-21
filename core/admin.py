from django.contrib import admin
from .models import UserCategoryPublishes,Likes,BanUserProduct,UserPhoto,UserCardInput,UserSocial


admin.site.register(UserCategoryPublishes)
admin.site.register(Likes)
admin.site.register(BanUserProduct)
admin.site.register(UserPhoto)
admin.site.register(UserCardInput)
admin.site.register(UserSocial)