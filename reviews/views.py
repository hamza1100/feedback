from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review

from django.views import View

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