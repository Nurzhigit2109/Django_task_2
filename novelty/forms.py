from django import forms
from novelty.models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'comment')
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Ваше имя"
                       }),
            "comment": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Ваш комментарий..."
                       }),
        }
