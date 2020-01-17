from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from artifacts.models import Artifact
from payment.models import OrderLineItem
from reviews.models import Review, ReviewLineItem
from reviews.forms import ReviewForm
    
# Views for the reviews in app
@login_required
def add_review(request, id):
    """
    View to add a review for an artifact, redirect back to view detail.
    """
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        
        if review_form.is_valid():
            review_artifact = review_form.save(commit=False)
            
            try:
                review_artifact.review_id = Review.objects.get(
                    artifact=id)
            except:
                review_artifact.review_id = Review.objects.create(
                    artifact=Artifact.objects.get(pk=id))
            
            review_artifact.review_owner_id = request.user.id
            review_artifact.review_date = timezone.now()
            review_artifact.save()
            
            messages.success(
                request,
                "You have successfully added a review for the artifact."
                )
        
        else:
            messages.error(
                request,
                "Sorry, there was a problem with your review submission."
                )
                
    else:
        review_form = ReviewForm()
        reviewed = False
        reviews = ReviewLineItem.objects.filter(review_id__artifact=id)
        artifact = Artifact.objects.get(id=id)
        ownership = OrderLineItem.objects.filter(artifact=id).filter(owner_id=request.user.id).first()
    
        if ownership != None:
            owner = True
            for review in reviews:
                if review.review_owner_id == ownership.owner_id:
                    reviewed = True
        else:
            owner = False
       
        return render (request, "review.html", {
            "artifact": artifact,
            "review_form": review_form,
            "reviews" : reviews,
            "owner": owner,
            "reviewed": reviewed,
            })
    
    return redirect("view_artifact", id=id)