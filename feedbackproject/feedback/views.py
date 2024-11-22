
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import FeedbackForm

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    feedbacks = item.feedback_set.all()
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.item = item
        feedback.save()
        return redirect('item_detail', item_id=item.id)
    return render(request, 'feedback/item_detail.html', {'item': item, 'feedbacks': feedbacks, 'form': form})
