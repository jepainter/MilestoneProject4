from django.shortcuts import render, redirect, reverse
from artifacts.models import Artifact
from histories.models import History, HistoryEvent
from histories.forms import HistoryEventForm

# Views for the histories in app
def view_history(request, id):
    """
    View to get data for display of history of artifact
    """
    event_form = HistoryEventForm()
    artifact = History.objects.filter(artifact_id=id)
    print("")
    for artifact_detail in artifact:
        print("## Artifact query ##")
        print("Artifact Name: " + str(artifact_detail.artifact.name))
        artifact_name=artifact_detail.artifact.name
        print("Artifact Id: " + str(artifact_detail.artifact.id))
        artifact_id=artifact_detail.artifact.id
        print("History Id: " + str(artifact_detail.id))
        history_id=artifact_detail.id
    print("artifact detail as variables assigned")
    print("Artifact Name: " + str(artifact_name))
    print("Artifact Id: " + str(artifact_id))
    print("Artifact History Id: " + str(history_id))
    
    
    print("Artifact: " + str(artifact))
    events = HistoryEvent.objects.filter(history_id=history_id)
    for event in events:
        print("")
        print("## Event query ##")
    #    print("Artifact ID :" + str(event.artifact.id))
    #   print("Artifact Name:" + str(event.artifact.name))
        print("Event Year: " + str(event.event_year))
        print("Event Era: " + str(event.event_era))
        print("Event Description: " + str(event.event_description))
    print("")
    print("Events: " + str(events))
    return render(request, "history.html", {
        "artifact_id": artifact_id,
        "artifact_name": artifact_name,
        "history_id": history_id,
        "events": events,
        "event_form": event_form,
        }
    )

def add_history_event(request, id):
    """
    View to add a history event to an artifact, redirect back to view history
    """
    print("")
    print("## Inside add history event ##")
    artifact_id = id
    print("Artifact Id")
    print(artifact_id)
    
    if request.method == "POST":
        event_form = HistoryEventForm(request.POST)
        
        if event_form.is_valid():
            event_year=request.POST["event_year"]
            event_era=request.POST["event_era"]
            event_description=request.POST["event_description"]
            history_id=request.POST["history_id"]
            print("")
            print("## Event form as submitted ##")
            print("Event year: " + str(event_year))
            print("Event era: " + str(event_era))
            print("Event description: " + str(event_description))
            print("History Id: " + str(history_id))
            
            event = HistoryEvent.objects.create(
                history_id_id=history_id,
                event_year=event_year,
                event_era=event_era,
                event_description=event_description
                )
            event.save()
            
        else:
            print("## ERROR: Form ##")
            print(event_form.errors)
    
    
    return redirect("view_history", id=id)