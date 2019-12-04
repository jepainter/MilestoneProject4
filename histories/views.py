from django.shortcuts import render
from artifacts.models import Artifact
from histories.models import History, HistoryEvent

# Views for the histories in app
def view_history(request, id):
    
    artifact = History.objects.filter(artifact_id=id)
    print("")
    for detail in artifact:
        print(detail.artifact.name)
        print(detail.artifact.id)
    
    print("Artifact: " + str(artifact))
    events = HistoryEvent.objects.filter(history_id=id)
    for event in events:
        print("")
        print("Event Year: " + str(event.event_year))
        print("Event Era: " + str(event.event_era))
        print("Event Description: " + str(event.event_description))
    print("")
    print("Events: " + str(events))
    return render(request, "history.html", {"artifact": artifact, "events": events})