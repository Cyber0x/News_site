from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class SearchResultView(ListView):
    model = Articles
    template_name = 'news/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Articles.objects.filter(
            Q(title__icontains=query) | Q(full_text__icontains=query)
        )
        return object_list


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/news_update.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена некорректно'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
