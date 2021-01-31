from mylib.queueNode import QueueNode


class Animal:
    def __init__(self, type_in, time_in):
        self.animal = type_in
        self.time = time_in


class Cat(Animal):
    def __init__(self, time_in):
        Animal.__init__(self, 'Cat', time_in)


class Dog(Animal):
    def __init__(self, time_in):
        Animal.__init__(self, 'Dog', time_in)


class AnimalShelter:
    def __init__(self):
        self.cats = QueueNode()
        self.dogs = QueueNode()
        self.time = 0

    def enqueue(self, type_in):
        self.time += 1
        if type_in.lower() == 'cat':
            # create a car
            new_cat = Cat(self.time)
            self.cats.enqueue(new_cat)
        elif type_in.lower() == 'dog':
            # create a dog
            new_dog = Dog(self.time)
            self.dogs.enqueue(new_dog)
        else:
            raise ValueError('Wrong animal type')

    def dequeue_any(self):
        if self.cats.is_empty():
            if self.dogs.is_empty():
                raise ValueError('Empty shelter')
            else:
                return self.dogs.dequeue()
        else:
            if self.dogs.is_empty():
                return self.cats.dequeue()
            else:
                # both Qs are full
                # return the oldest animal
                if self.cats.peek().time > self.dogs.peek().time:
                    # dog is older
                    return self.dogs.dequeue()
                else:
                    # cat is older
                    return self.cats.dequeue()

    def dequeue_dog(self):
        if self.dogs.is_empty():
            raise ValueError('Sorry, there is no dogs')
        return self.dogs.dequeue()

    def dequeue_cat(self):
        if self.cats.is_empty():
            raise ValueError('Sorry, there is no cats')
        return self.cats.dequeue()

    def peek(self):
        if self.cats.is_empty():
            if self.dogs.is_empty():
                raise ValueError('Empty shelter')
            else:
                return self.dogs.peek()
        else:
            if self.dogs.is_empty():
                return self.cats.peek()
            else:
                # both Qs are full
                # return the oldest animal
                if self.cats.peek().time > self.dogs.peek().time:
                    # dog is older
                    return self.dogs.peek()
                else:
                    # cat is older
                    return self.cats.peek()

    def size(self):
        return self.cats.size() + self.dogs.size()

    def is_empty(self):
        return self.cats.is_empty() and self.cats.is_empty()
