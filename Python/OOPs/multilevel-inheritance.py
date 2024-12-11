class car:
    def start(self):
        print("started car...")    

class toyota(car):
    def stop(self):
        print("stopped toyota...")

class fortuner(toyota):
    pass

a1 = fortuner()
a1.start()
a1.stop()

# Car -> Toyota -> fortuner