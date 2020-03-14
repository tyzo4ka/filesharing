from urllib.parse import urlencode
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from webapp.views.base_views import SearchFilesView
from webapp.models import File
from webapp.forms import FileSearchForm, FileForm, AnonFileForm


class IndexView(SearchFilesView):
    queryset = File.objects.filter(access="Public")
    model = File
    template_name = 'file/list.html'
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 2
    search_form = FileSearchForm

    def get_filters(self):
        return Q(caption__icontains=self.search_value)


class FileView(DetailView):
    model = File
    template_name = "file/detail.html"


class FileCreate(CreateView):
    model = File
    template_name = 'file/create.html'
    form_class = None

    def get_form_class(self, form_class=None):
        if self.request.user.is_anonymous:
            self.form_class = AnonFileForm
        else:
            self.form_class = FileForm
        return self.form_class

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.request.user.is_anonymous:
            self.object.author = None
        else:
            self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})


class FileUpdate(PermissionRequiredMixin, UpdateView):
    model = File
    template_name = 'file/update.html'
    fields = ['file', 'caption', 'access']
    permission_required = "webapp.change_file"
    permission_denied_message = "Permission denied"

    def is_author(self):
        return self.get_object().author == self.request.user

    def has_permission(self):
        return super().has_permission() or self.is_author()

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})


class FileDelete(PermissionRequiredMixin, DeleteView):
    model = File
    template_name = "file/delete.html"
    success_url = reverse_lazy('webapp:index')
    permission_required = "webapp.delete_file"
    permission_denied_message = "Permission denied"

    def is_author(self):
        return self.get_object().author == self.request.user

    def has_permission(self):
        return super().has_permission() or self.is_author()

    def get_success_url(self):
        return reverse('webapp:index')
