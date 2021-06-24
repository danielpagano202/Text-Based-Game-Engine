class GameObject:
    #Origin stage / Stage that this Game Object is located on
    stage = None
    #Position on stage
    x = 0
    y = 0
    #Z axis (Highest order is above the others when intersecting)
    order = 0
    #Width and height of text
    width = 0
    height = 0
    #Text that makes up the visual part of the gameobject
    text = ""
    #Array that has the position of every character except for spaces (In the order of top left to bottom right and is vital for many functions to work)
    positions = []
    #Index of the object in the stage's objects list
    index = 0
    #Tag that can be used to uniquely identify a gameobject
    tag = ""
    def __init__(self, stage, x, y, order, width, height, text, positions, index):
        self.stage = stage
        self.x = x
        self.y = y
        self.order = order
        self.width = width
        self.height = height
        self.text = text
        self.positions = positions
        self.index = index
    def __str__(self):
        return self.text
    #Fixes or creates the positions in the positions array.
    def regeneratepositions(self):
        self.positions = []
        workinglist = self.text.split("\n")
        for i in range(len(workinglist)):
            if len(workinglist[i]) != self.width:
                workinglist[i] += (" " * (self.width - len(workinglist[i])))
        self.text = ''.join(str(x) + "\n" for x in workinglist)
        for h in range(self.height):
            for w in range(self.width):
                if workinglist[h][w] != " " and workinglist[h][w] != "":
                    self.positions.append(str(w) + ":" + str(h))
    #These two function flip it on the x or y axis respectively
    def xflip(self):
        self.delete()
        textlist = [""] * self.height
        for h in range(self.height):
            for w in range(self.width - 1, -1, -1):
                textlist[h] = textlist[h] + self.text.split("\n")[h][w]
        self.text = str("".join(textlist[x] + "\n" for x in range(len(textlist))))
        self.regeneratepositions()
        self.stage.placeobject(self)
    def yflip(self):
        self.delete()
        textlist = []
        for i in range(self.height - 1, -1, -1):
            textlist.append(self.text.split("\n")[i])
        self.text = ''.join(x + "\n" for x in textlist)
        self.regeneratepositions()
        self.stage.placeobject(self)
    #These two functions rotate the text 90 degrees either right or left
    def rightrotate(self):
        self.delete()
        oldwidth = self.width
        oldheight = self.height
        textlist = [""] * self.width
        for h in range(self.height - 1, -1, -1):
            for w in range(self.width):
                    textlist[w] = textlist[w] + self.text.split("\n")[h][w]
        self.text = str("".join(textlist[x] + "\n" for x in range(len(textlist))))
        self.width = oldwidth
        self.height = oldheight
        self.regeneratepositions()
        self.stage.placeobject(self)
    def leftrotate(self):
        self.delete()
        textlist = [""] * self.width
        for h in range(self.height - 1, -1, -1):
            for w in range(self.width):
                textlist[w] = textlist[w] + self.text.split("\n")[h][w]
        textlist = [x for x in reversed(textlist)]
        templist = textlist
        textlist = []
        for x in templist:
            textlist.append(x[::-1])
        self.text = str("".join(textlist[x] + "\n" for x in range(len(textlist))))
        self.regeneratepositions()
        self.stage.placeobject(self)
    #Moves the object relative to its position and will return whether it collides or not
    def push(self, x, y, collides = False):
        if collides:
            if self.detectallcollisions():
                return True
        self.delete()
        self.x += x
        self.y += y
        self.stage.placeobject(self)
        return False
    #Moves the object to a position on the board based on x and y
    def move(self, x, y):
        self.stage.delete(self.index)
        self.x = x
        self.y = y
        return self.stage.placeobject(self)
    #Deletes the game object
    def delete(self):
        gtext = ""
        for i in range(self.height):
            if i != 0:
                gtext = gtext + "\n"
            gtext = gtext + (self.stage.character * self.width)
        self.stage.objects.pop(self.index)
        textasset = TextAsset(gtext)
        self.stage.place(textasset, self.x, self.y, self.order)
    #This replace a character at a certain position on the text. (0, 0) is the top left character always
    def replacecharacter(self, x, y, new):
        if len(new) > 1:
            raise Exception(" 'New' has a value of more than one character. Replace each character individually.")
        copy = list(self.text.split("\n"))
        copyline = list(copy[y])
        copyline[x] = str(new)
        copy[y] = ''.join(copyline)
        self.text = "".join(["".join(i) + "\n" for i in copy])
        self.delete()
        self.stage.placeobject(self)
    #This replaces a group of characters based on the corners given
    def replacecharacters(self, top, right, bottom, left, new):
        for y in range(top, bottom + 1, 1):
            for x in range(left, right, 1):
                self.replacecharacter(x, y, new)
    #This deletes a character at a certain position on the text. (0, 0) is the top left character always
    def deletecharacter(self, x, y):
        self.replacecharacter(x, y, self.stage.character)
    #This deletes a group of characters based on the corners given
    def deletecharacters(self, top, right, bottom, left):
        self.replacecharacters(top, right, bottom, left, self.stage.character)
    #This detects the collision with one other game object
    def detectcollision(self, obj):
        if obj.order != self.order:
            return False
        this = self.positions
        other = obj.positions
        current = lambda string, index, addition : int(string.split(":")[index]) + addition
        for i in range(len(this)):
            currentx = current(this[i], 0, self.x)
            currenty = current(this[i], 1, self.y)
            this[i] = str(currentx) + ":" + str(currenty)
        for i in range(len(other)):
            currentx = current(other[i], 0, obj.x)
            currenty = current(other[i], 1, obj.y)
            other[i] = str(currentx) + ":" + str(currenty)
        if len(set(this).intersection(set(other))) > 0:
            return True
        return False
    #This detects if any game object
    def detectallcollisions(self):
        #This checks all collisions. We use a counter to check for if there are two times where objects will collide since it will collide with itself once
        counter = 0
        objects = []
        for i in self.stage.objects:
            if self.detectcollision(i):
                counter = counter + 1
            if counter == 2:
                objects.append(i)
        return objects