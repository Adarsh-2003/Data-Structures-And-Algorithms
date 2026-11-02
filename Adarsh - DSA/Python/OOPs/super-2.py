class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class programmer(employee):
    def __init__(self,name,id,lang):
        self.name = name
        self.id= id
        self.lang = lang

# to reduce redundancy and increase reuseability

class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class programmer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

