from .views import TopicView, AddTopicView, DeleteTopicView, TopicDetailView, ReplyAddView
from django.urls import path, re_path


urlpatterns =[
    path('', TopicView.as_view(), name='index'),
    path('add', AddTopicView.as_view(), name='add'),
    re_path(r'delete/(?P<topic_id>\d+)/', DeleteTopicView.as_view(), name='delete'),
    re_path(r'detail/(?P<topic_id>\d+)', TopicDetailView.as_view(), name='detail'),
    path('replyadd', ReplyAddView.as_view(), name='replyadd')
]