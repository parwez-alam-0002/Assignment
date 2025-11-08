class Dog:
    def __init__(self,name,breed,property):
        self.name=name
        self.breed=breed
        self.property=property
        print('--------------------------')

    def bark(self):
        print("WOOOO!...")
    
    def sleep(self,property):
        self.property=property
        print(f"{self.name} is {self.property}...")

    def wake(self,property):
        self.property=property
        print(f'{self.name} is {self.property}...')

    def display(self):
        print(f'Breed is {self.breed}  and named is {self.name}. ')

dog1=Dog("Lucky",'Dobermann','Sleeping')
dog1.display()
dog1.bark()
dog1.wake("Waking")
dog1.sleep("sleeping")

dog2=Dog("Rush",'Bulldog','Sleeping')
dog2.display()
dog2.bark()
dog2.wake("Waking")
dog2.sleep("sleeping")

