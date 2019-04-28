from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.urls import reverse
from .models import Topic, Reply
# Create your views here.


class TopicView(View):
    def get(self, request):
        all_topic = Topic.objects.all()
        return render(request, 'topic/index.html', {"all_topic": all_topic, })


class AddTopicView(View):
    def get(self, request):
        return render(request, 'topic/new.html', {})

    def post(self, request):
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        topic_add = Topic()
        topic_add.title = title
        topic_add.content = content
        topic_add.user = request.user
        topic_add.save()
        return redirect(reverse('mytopic:detail', kwargs={'topic_id': topic_add.id}))


class DeleteTopicView(View):
    def get(self, request, topic_id):
        topic = Topic.objects.filter(id=topic_id)
        topic.delete()
        return redirect(reverse('mytopic:index'))


class TopicDetailView(View):
    def get(self, request, topic_id):
        topic = Topic.objects.get(id=topic_id)
        topic.views += 1
        topic.save()
        reply = Reply.objects.filter(topic=topic)
        print(reply)
        reply_num = len(reply)
        return render(request, 'topic/detail.html', {'topic': topic, 'reply_num': reply_num, 'reply':reply})


class ReplyAddView(View):
    def post(self, request):
        content = request.POST.get('content', '')
        user = request.user
        topic_id = request.POST.get('topic_id', '')
        print(topic_id)
        topic = Topic.objects.get(id=topic_id)
        reply = Reply()
        reply.content = content
        reply.user = user
        reply.topic = topic
        reply.save()
        return redirect(reverse('mytopic:detail', kwargs={'topic_id': topic_id}))
