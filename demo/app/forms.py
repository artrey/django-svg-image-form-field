from django import forms

from .models import Article
from django_svg_image_form_field import SvgAndImageFormField


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = []
        field_classes = {
            'image': SvgAndImageFormField,
        }
