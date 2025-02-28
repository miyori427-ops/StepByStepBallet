from django.contrib import admin
from django.urls import include, path
from . import views  # 同じディレクトリにあるviews.pyをインポート

app_name = 'technique'


urlpatterns = [
    path('', views.indexa, name='indexa'),
    path('indexb/', views.indexb, name='indexb'),
    #path('indexb/<int:id>/', views.indexb, name='indexb'),
    #path('indexmove/', views.indexmove, name='indexmove'),
    path('indexmove', views.indexmove, name='indexmove'),
    path('index2/', views.index2, name='index2'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")) ,# accounts.urls.pyを読み込むための設定を追加
    path('signup/', views.signup, name="signup"),
]