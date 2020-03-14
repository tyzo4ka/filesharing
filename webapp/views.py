from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import File


class IndexView(ListView):
    model = File
    template_name = 'file/list.html'
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 2


class FileView(DetailView):
    model = File
    template_name = "file/detail.html"


class FileCreate(CreateView):
    model = File
    # form_class = ArticleForm
    template_name = 'file/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def save_tags(self, tags):
        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            self.object.tags.add(tag)

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})
