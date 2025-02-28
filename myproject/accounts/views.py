from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm # ログインフォームをimport


class IndexView(TemplateView):
    """ ホームビュー """
    template_name = "index.html"


class SignupView(CreateView):
    """ ユーザー登録用ビュー """
    form_class = SignUpForm # 作成した登録用フォームを設定
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("technique:indexa") # ユーザー作成後のリダイレクト先ページ



    def form_valid(self, form):
        # フォームが有効な場合の処理
        response = super().form_valid(form)  # 必ずこれを呼び出す
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        if user:
            login(self.request, user)  # ユーザーをログイン状態にする
        return response
# ログインビューを作成
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

# LogoutViewを追加
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")




