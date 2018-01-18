from django import forms
from .models import Post
from django.utils.text import slugify
import itertools
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    content=forms.CharField(widget=PagedownWidget)

    class Meta:
        model=Post
        fields=["title","content","file"]

    def save(self,commit=True):
        instance = super(PostForm, self).save(commit=False)

        instance.slug = orig = slugify(instance.title)

        for x in itertools.count(1):
            if not Post.objects.filter(slug=instance.slug).exists():
                break
            instance.slug = '%s-%d' % (orig, x)

        instance.save()

        return instance