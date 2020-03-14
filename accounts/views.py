from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from webapp.models import File
from .forms import UserCreationForm


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'user_create.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    # def get_context_data(self, **kwargs):
    #     print("kfkkfkfkkf")
    #     context = super().get_context_data()
    #     user = User.objects.get(pk=self.kwargs['pk'])
    #     context['self_files'] = File.objects.filter(author=user.pk)
    #     print(context)
    #     # context['files'] = File.objects.order_by('created_at')
    #     return context

