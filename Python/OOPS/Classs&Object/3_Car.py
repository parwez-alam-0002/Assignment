class Car:
    def __init__(self,brand,model,millage):
        self.brand=brand
        self.model=model
        self.millage=millage 

    def display_info(self):
        print(f'Brand : {self.brand}')
        print(f'Model : {self.model}')
        print(f'Millage : {self.millage}')

    def start(self):
        print("Car is running...")

    def stop(self):
        print("Car is stopped...")

maruti=Car("Maruti",'Suzuki Swift','25.75 kmpl')

maruti.display_info()
maruti.start()
maruti.stop()
