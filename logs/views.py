from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Topic, Entry, Link
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm, DeleteEntryForm, DeleteTopicForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    t = Topic.objects.order_by("title")
    context = {'topics':t}
    return render(request, "index.html", context)
    #return HttpResponse("<h1>Hello Django</h1>")


@login_required
def topics(request):
    t = Topic.objects.order_by("title")
    context = {"topics": t}
    return render(request, "topics.html", context)


def resources(request):
    topics = Topic.objects.all()
    topics_links = {}
    for t in topics:
        links = t.link_set.all()
        topics_links[t] = links
    context = {"topics":topics_links} # topics_links ={topic1: links, topic2: links....}

    return render(request, "resources.html", context)


@login_required
def topic(request, topic_id):
    '''show a single topic and all its entries'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {"topic":topic, "entries": entries}
    return render(request,"topic.html", context )


@login_required
def new_topic(request):
    '''Add a new topic'''
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logs:topics'))
    context = {'form': form}
    return render(request, 'new_topic.html', context)


@login_required
def edit_topic(request, topic_id):
    '''Edit a new topic'''
    topic = Topic.objects.get(id = topic_id)
    num = len(topic.entry_set.all()) # number of entries under this topic
    if request.method != 'POST':
        form = TopicForm(instance = topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("logs:topic", args=[topic.id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'edit_topic.html', context)


@login_required
def new_entry(request, topic_id):
    '''Add a new entry for a particular topic'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    '''Edit an existing entry.'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance =entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)


@login_required
def delete_entry(request, entry_id):
    '''delete an existng entry.'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    entry_to_delete = get_object_or_404(Entry, id=entry_id)

    if request.method!='POST':
        form = DeleteEntryForm(instance=entry)
    else:
        form = DeleteEntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            entry_to_delete.delete()
            return HttpResponseRedirect(reverse('logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'delete_entry.html', context)


@login_required
def delete_topic(request, topic_id):
    '''delete an existng topic.'''
    topic = Topic.objects.get(id=topic_id)
    topic_to_delete = get_object_or_404(Topic, id=topic_id)
    if request.method != 'POST':
        form = DeleteTopicForm(instance=topic)
    else:
        form = DeleteTopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            topic_to_delete.delete()
            return HttpResponseRedirect(reverse('logs:topics'))
    context = {'topic': topic, 'form': form}
    return render(request, 'delete_topic.html', context)
