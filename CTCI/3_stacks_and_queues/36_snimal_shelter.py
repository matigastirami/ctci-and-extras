from CTCI.helpers.queues import Queue
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'{self.get_type()}(name: {self.name})'

    def get_type(self) -> str:
        return "animal"

class Dog(Animal):
    def get_type(self) -> str:
        return 'dog'

class Cat(Animal):
    def get_type(self) -> str:
        return 'cat'

class AnimalShelter:
    def __init__(self):
        self.queues = [Queue(), Queue()]
        self.current_queue = 0

    def __str__(self):
        return self.queues[self.current_queue].__str__()

    def enqueue(self, animal: Animal):
        self.queues[self.current_queue].push(animal)

    def dequeueAny(self):
        return self.queues[self.current_queue].pop()

    def dequeueDog(self):
        while self.queues[self.current_queue].peek().get_type() != 'dog' and not self.queues[self.current_queue].is_empty():
            self.queues[1 - self.current_queue].push(self.queues[self.current_queue].pop())

        dog = self.queues[self.current_queue].pop()
        remaining = self.queues[self.current_queue].pop()

        while remaining:
            self.queues[1 - self.current_queue].push(remaining)
            remaining = self.queues[self.current_queue].pop()

        self.current_queue = 1 - self.current_queue
        return dog

    def dequeueCat(self):
        while self.queues[self.current_queue].peek().get_type() != 'cat' and not self.queues[self.current_queue].is_empty():
            self.queues[1 - self.current_queue].push(self.queues[self.current_queue].pop())

        cat = self.queues[self.current_queue].pop()
        remaining = self.queues[self.current_queue].pop()

        while remaining:
            self.queues[1 - self.current_queue].push(remaining)
            remaining = self.queues[self.current_queue].pop()

        self.current_queue = 1 - self.current_queue
        return cat

def test_animal_shelter():
    shelter = AnimalShelter()

    # Enqueue a sequence of dogs and cats
    shelter.enqueue(Dog("Rex"))
    shelter.enqueue(Cat("Whiskers"))
    shelter.enqueue(Dog("Fido"))
    shelter.enqueue(Cat("Mittens"))
    shelter.enqueue(Dog("Bruno"))

    # Dequeue Any → should be Rex
    assert shelter.dequeueAny().name == "Rex"

    # Dequeue Cat → should be Whiskers
    assert shelter.dequeueCat().name == "Whiskers"

    # Dequeue Dog → should be Fido
    assert shelter.dequeueDog().name == "Fido"

    # Dequeue Any → should be Mittens (cat)
    assert shelter.dequeueAny().name == "Mittens"

    # Dequeue Dog → should be Bruno
    assert shelter.dequeueDog().name == "Bruno"

    # Queue should be empty now
    try:
        shelter.dequeueAny()
        assert False, "Expected empty shelter"
    except Exception:
        pass

    print("✅ AnimalShelter tests passed.")

if __name__ == "__main__":
    test_animal_shelter()
