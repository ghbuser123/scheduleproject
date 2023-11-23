from django.forms import ModelForm
from .models import SchedulePost
from django import forms


# 新規イベント追加フォーム
class SchedulePostForm(ModelForm):
    class Meta:
        model = SchedulePost
        fields = ['category','title','start_date','end_date','memo']
        widgets = {
            'start_date': forms.NumberInput(attrs={"type": "date"}),
            'end_date' : forms.NumberInput(attrs={"type": "date"})
        }

# お問い合わせフォーム
class EmailmeForm(forms.Form): 
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__(self,*args,**kwarge):
        super().__init__(*args,**kwarge)

        self.fields['name'].widget.attrs['placeholder'] = \
            'お名前を入力してください'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = \
            'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = \
            'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder'] = \
            'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'