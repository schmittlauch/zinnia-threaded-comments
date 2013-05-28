"""Forms for zinnia-threaded-comments"""
from django import forms
from django.contrib.comments.forms import CommentForm

from zinnia_threaded_comments.models import ThreadedComment

from captcha.fields import ReCaptchaField


class ThreadedCommentForm(CommentForm):
    """
    Threaded comment form
    """
    parent = forms.ModelChoiceField(
        queryset=ThreadedComment.objects.all(),
        widget=forms.HiddenInput(),
        required=False)

    captcha = ReCaptchaField()

    def get_comment_model(self):
        return ThreadedComment

    def get_comment_create_data(self):
        data = super(ThreadedCommentForm, self).get_comment_create_data()
        data['parent'] = self.cleaned_data['parent']
        return data
