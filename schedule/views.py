from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SchedulePostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import SchedulePost
from django.views.generic import DeleteView
from django.views.generic import FormView
from .forms import EmailmeForm
from django.contrib import messages
from django.core.mail import EmailMessage


# トップページのビュー
class IndexView(TemplateView):
    template_name = 'index.html'

# デコレーターにより、アクセスはログインユーザーに限定される
@method_decorator(login_required,name='dispatch')

# スケジュール登録ページのビュー
class CreateScheduleView(CreateView):
    form_class = SchedulePostForm
    template_name = "entry_schedule.html"

    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('schedule:entry_done')

    def form_valid(self,form):
        # commit=Falseにしてpostされたデータ取得
                entrydata = form.save(commit=False)
        # ユーザーのid取得してモデルのuserフィールドに格納
                entrydata.user = self.request.user
        # データをデータベースに登録
                entrydata.save()
                return super().form_valid(form)

# イベント追加完了ページのビュー
class EntrySuccessView(TemplateView):
    template_name = 'entry_success.html'     

# マイページのビュー
class MypageView(ListView):
    template_name = 'mypage.html'

    def get_queryset(self):
        queryset = SchedulePost.objects.filter(user=self.request.user)
        return queryset

# Emailme(お問い合わせ)ページのビュー p.290~293
class EmailmeView(FormView):
    template_name = 'emailme.html'
    form_class = EmailmeForm

    success_url = reverse_lazy('schedule:emailme')

    # フォームに入力されたデータをフィールド名を指定して取得
    def form_valid(self,form):
        # フォーム入力されたデータを取得
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        
        # メールのタイトルの書式設定
        subject = 'Email me: {}'.format(title)
        # フォームの入力データの書式設定
        message = \
            '送信者名: {0}\n メールアドレス: {1}\n タイトル: {2}\n メッセージ: \n{3}'\
                .format(name,email,title,message)

        # メールの送信元のアドレス
        from_email = 'chocobo112917@gmail.com'
        # 送信先のメールアドレス(自分)
        to_list = ['mit2371080@stu.o-hara.ac.jp']
        # emailmessageオブジェクトを生成
        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,)
        # EmailMessageクラスのsend()によってメールサーバーからメール送信
        message.send()
        # 送信完了後に表示
        messages.success(self.request,'メールは正常に送信されました。')

        return super().form_valid(form)        