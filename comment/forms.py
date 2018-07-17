from django.forms import ModelForm, Textarea
from .models import Comment

app_label = 'comment'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['text'].widget = Textarea(attrs={
            'class': 'textarea',
            'rows': 1,
            'type': 'text',
            'placeholder': 'What do you think of this product...'
        })

