from django.shortcuts import render
from django.utils import timezone
from artifacts.models import Artifact
from histories.models import HistoryEvent
from bids.models import BidEvent, BidLineItem
#from categories.models import Category

# Views for the artifacts in app
def all_artifacts(request):
    """
    Function to call all instances of artifacts and render to page
    """
    artifacts = Artifact.objects.all()
#    categories = Category.objects.all()
    return render(request, "artifacts.html", {"artifacts": artifacts})

def view_artifact(request, id):
    """
    Function to view detail relating to artifact, such as history,
    bid information
    """
    
    #artifact = Artifact.objects.filter(id=id)
    history_events = HistoryEvent.objects.filter(history_id__artifact=id)
    
    try:
        bid_event = BidEvent.objects.get(artifact=id)
       # bid_event_status = bid_event.bid_event_status
        #bid_event_deadline = bid_event.bid_event_deadline
        artifact = bid_event.artifact
        print("Checking bid detail")
        print(bid_event)
    
    except:
        print("No bid event exists2")
        bid_event_status = "Bidding Closed"
        bid_event = ""
        artifact = Artifact.objects.get(id=id)
        
    
    
    try:
        bid_line_item = BidLineItem.objects.filter(bid_user=request.user.id).get(bid_event__artifact=id)
    except:
        bid_line_item = ""
    
    if bid_line_item:
        print("Bid placed by user")
        print(bid_line_item)
    else:
        print("No bid for user")
        print(bid_line_item)
        
    cart = request.session.get("cart", {})
    print("Cart: "+ str(cart))
    
    artifact_in_cart = {}
    for artifact_id, artifact_quantity in cart.items():
        if artifact_id == id:
            artifact_in_cart = {
                "artifact_id" : artifact_id,
                "artifact_quantity": artifact_quantity,
                }
    
    print("Artifact in cart : " + str(artifact_in_cart))
    
    #    return render(request, "artifact_detail.html", {
    #    "artifact": artifact,
    #    "bid_event_status": bid_event_status,
    #    "events": events,
    #    })
        
    
    #for detail in events:
    #    print(detail.history_id.artifact.id)
    #    artifact = detail.history_id.artifact
    #    artifact_id = detail.history_id.artifact.id
    #    artifact_description = detail.history_id.artifact.description
    #    artifact_category = detail.history_id.artifact.category.category_description
    
    #print("------")
    #print("## Inside the view artifact function ##")
 #   print("Artifact: " + str(artifact))
 #   for artifact_detail in artifact:
  #      print("Artifact Name: " + str(artifact_detail.history_id.artifact.id))
    #    print("Artifact Id: " + str(artifact_detail.id))
    #    print("Category Object: " + str(artifact_detail.category))
    #    print("Category Id: " + str(artifact_detail.category.id))
    #    print("Category Description: " + str(artifact_detail.category.category_description))
    
    #category = Category.objects.filter(category_name=artifact_detail.category)
    #categories = Category.objects.all()
    
    #print("")
    #print("Testing access from artifact to category via foreignkey")
   # print("Artifact: " + str(artifact))
    
    
    #print("Exit test")
    #print("")
    
    
    #print("Category: " + str(category))
    
    
    #artifact_h = HistoryEvent.objects.filter(history_id=id)
    
    return render(request, "artifact_detail.html", {
        "artifact": artifact,
        "bid_event": bid_event,
     #   "bid_event_deadline": bid_event_deadline,
        "datetime": timezone.now(),
        "history_events": history_events,
        "bid_line_item" : bid_line_item,
        "artifact_in_cart": artifact_in_cart
        })