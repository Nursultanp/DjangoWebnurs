from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма туура эмес толтурулду'



    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
