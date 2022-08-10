from observer import Observer

class Output(Observer):
    def __init__(self, *sources):
        super().__init__()
        for source in sources:
            source.subscribe(self)

    def on_event(self, event):
        if event.action == 'die':
            print(event.source.name, 'died!')
        else:
            print(event.source.name, event.value)