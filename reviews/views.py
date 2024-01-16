from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        
        return render(request, 'reviews/review.html', {
            'form': form
        })

# def review(request):
#     if request.method == 'POST':
#         # below two lines can be used to update an existing record instead of creating a new
#         # existing_data = Review.objects.get()
#         # form = ReviewForm(request.POST, instance=existing_data)
#         form = ReviewForm(request.POST)
#         print('is form valid? :', form.is_valid())
#         if form.is_valid():
#             # since this is a model form. we can directly save the data into the model.
#             form.save()
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review_text=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating'])
#             # review.save()
#             print('entered name :', form.cleaned_data)
#             return HttpResponseRedirect('/thank-you')
        
#     else:
#         form = ReviewForm()

#     form = ReviewForm()
#     return render(request, 'reviews/review.html', {
#         'form': form
#     })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello World!'
        return context
    
class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review

    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     selected_review = Review.objects.get(pk=review_id)
    #     context['review'] = selected_review
    #     return context