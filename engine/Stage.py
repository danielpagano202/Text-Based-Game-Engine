class Stage:
    height = 8
    width = 8
    character = "0"
    board = []
    futureboard = []
    objects = []
    def __init__(self, height, width, character):
        self.height = height
        self.width = width
        self.character = character
        self.board = [""] * self.height
        if len(character) > 1:
            raise Exception("Error: Character for stage provided has a length of more than one")
        for h in range(self.width):
            for w in range(self.height):
                self.board[h] += self.character
        self.futureboard = list(self.board)
    def __str__(self):
        return ''.join(str(x) + "\n" for x in self.board)
    #Prints the text with it defaulting to rebuilding and generating the new frame
    def print(self, rebuild=True, generateframe=True):
        if rebuild:
            self.fullrebuild()
        if generateframe:
            self.generateframe()
        for i in self.board:
            print(i)
    #This changes the future board (which contains the next frame's content)
    def generateframe(self):
        self.board = list(self.futureboard)
    #This places a text asset on the stage, effectively turning it into a game object
    def place(self, textasset, x, y, order):
        for i in textasset.positions:
            infox = int(i.split(':')[0])
            infoy = int(i.split(':')[1])
            rowlist = list(self.futureboard[y + infoy])
            rowlist[x + infox] = textasset.text.split('\n')[infoy][infox]
            self.futureboard[y + infoy] = ''.join(rowlist)
        self.objects.append(GameObject(self, x, y, order, textasset.width, textasset.height, textasset.text, textasset.positions, len(self.objects)))
        return self.objects[len(self.objects) - 1]
    #This places a game object on the stage. Not recommended to use to place something on the stage
    def placeobject(self, obj):
        return self.place(TextAsset(obj.text), obj.x, obj.y, obj.order)
    #Rebuilds the stage as an empty
    def rebuild(self):
        self.futureboard = [""] * self.height
        for h in range(self.width):
            for w in range(self.height):
                self.futureboard[h] += self.character
    #Rebuilds all of the objects in the order of lowest order value to highest
    def rebuildobjects(self):
        orders = [self.objects[x].order for x in range(len(self.objects))]
        #This looks stupid because self.objects is already a list but without it, self.objects just disappears. IDK why.
        objs = list(self.objects)
        sorted(orders)
        def getorder(e):
            objs = self.objects
            return objs[objs.index(e)].order
        objs.sort(key=getorder)

        self.objects = []
        for i in range(len(orders)):
            self.placeobject(objs[i])
    #Calls rebuild and rebuildobjects
    def fullrebuild(self):
        self.rebuild()
        self.rebuildobjects()