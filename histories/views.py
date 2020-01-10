from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from artifacts.models import Artifact
from histories.models import History, HistoryEvent
from histories.forms import HistoryEventForm
from payment.models import OrderLineItem
    
# Views for the histories in app
@login_required
def view_history(request, id):
    """
    View to get data for display of history of artifact.
    """
    
    event_form = HistoryEventForm()
    history_events = HistoryEvent.objects.filter(history_id__artifact=id)
    ownership = OrderLineItem.objects.filter(artifact=id).filter(owner_id=request.user.id).first()
    
    if ownership != None:
        owner = True
    else:
        owner = False
    
    try:
        artifact_history = History.objects.get(artifact=id)
    except:
        artifact_history = ""
        try:
            artifact = Artifact.objects.get(pk=id)
        except:
            messages.error(
                request,
                "Sorry, that artifact history is not available."
                )
            return redirect(reverse("artifacts"))
    
    return render(request, "history.html", {
        "artifact_id": id,
        "history_events": history_events,
        "artifact_history": artifact_history,
        "event_form": event_form,
        "owner": owner,
        })


@login_required
def add_history_event(request, id):
    """
    View to add a history event to an artifact, redirect back to view history.
    """
    
    if request.method == "POST":
        event_form = HistoryEventForm(request.POST)
        
        if event_form.is_valid():
            history_event = event_form.save(commit=False)
            
            try:
                history_event.history_id = History.objects.get(
                    id=request.POST["history_id"])
            except:
                history_event.history_id = History.objects.create(
                    artifact=Artifact.objects.get(id=id))
        
            history_event.save()
            messages.success(
                request,
                "You have successfully added a history event."
                )
        
        else:
            messages.error(
                request,
                "Sorry, there was a problem with your submission."
                )
    
    return redirect("view_history", id=id)