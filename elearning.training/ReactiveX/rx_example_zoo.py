from observable import Observable
import asyncio
import random

class AnimalEvent:
    def __init__(self, source, action, value = ''):
        self.source = source
        self.action = action
        self.value = value

class Animal(Observable):
    def __init__(self, name, sound):
        super().__init__()
        self.name = name
        self. sound = sound

    async def run(self):
        while True:
            await asyncio.sleep(random.random() * 10)

            if random.random() < 0.01:
                self._event(AnimalEvent(self, 'die'))
                self._complete()
                return

            self._event(AnimalEvent(self, 'noise', self.sound))