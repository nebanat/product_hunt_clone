from django.urls import path
from django.views.decorators.http import require_POST
from .views import CommentFormView

app_name = 'comment'

urlpatterns = [
    path('new', require_POST(CommentFormView.as_view()), name='new')
]
