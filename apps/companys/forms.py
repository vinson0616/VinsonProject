import re

from django import forms
from .models import UserMessage


class UserMessageForm(forms.ModelForm):

    class Meta:
        model = UserMessage
        fields = ['name', 'title', 'mobile', 'email', 'content']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1(3|4|5|6|7|8)\d{9}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")