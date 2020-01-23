from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from artifacts.models import Artifact
from bids.models import BidEvent, BidLineItem
from histories.models import HistoryEvent
from payment.models import OrderLineItem
from reviews.models import ReviewLineItem


# Views for the artifacts in app
def all_artifacts(request):
    """
    Function to call all instances of artifacts and render to page.
    """
    artifacts = Artifact.objects.all()
    
    return render(request, "artifacts.html", {"artifacts": artifacts})


def view_artifact(request, id):
    """
    Function to view detail relating to artifact, such as history,
    bid information and reviews. Nested try except loops to reduce 
    calls to database if possible. Checks current cart for an existing 
    artifact in order to render relevant options in html (bid or purchase).
    """
    # Retrieval of bid information and artifact for display
    try:
        bid_line_item = BidLineItem.objects.filter(
            bid_user=request.user.id).get(bid_event__artifact=id)
        bid_event = bid_line_item.bid_event
        artifact = bid_line_item.bid_event.artifact
    except:
        bid_line_item = ""
        # Retrieval of artifact detail if above try fails
        try:
            bid_event = BidEvent.objects.get(artifact=id)
            artifact = bid_event.artifact
        except:
            bid_event = ""
            artifact = get_object_or_404(Artifact, pk=id)
    
    # Check if item in cart to determine bidding and purchasing options
    cart = request.session.get("cart", {})
    artifact_in_cart = {}
    for artifact_id, artifact_quantity in cart.items():
        if artifact_id == id:
            artifact_in_cart = {
                "artifact_id" : artifact_id,
                "artifact_quantity": artifact_quantity,
                }
    
    # Check to determine if user is owner and determine if user have reviewed           
    history_events = HistoryEvent.objects.filter(
        history_id__artifact=id).order_by("event_era").order_by("event_year")
    ownership = OrderLineItem.objects.filter(
        artifact=id).filter(owner_id=request.user.id).first()
    reviews = ReviewLineItem.objects.filter(review_id__artifact=id)
    reviewed = False
    if ownership != None:
        owner = True
        for review in reviews:
            if review.review_owner_id == ownership.owner_id:
                reviewed = True
    else:
        owner = False
    
    return render(request, "artifact_detail.html", {
        "artifact": artifact,
        "bid_event": bid_event,
        "datetime": timezone.now(),
        "history_events": history_events,
        "reviews": reviews,
        "bid_line_item" : bid_line_item,
        "artifact_in_cart": artifact_in_cart,
        "owner": owner,
        "reviewed": reviewed,
        })