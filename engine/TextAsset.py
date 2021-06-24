class TextAsset:
    width = 0
    height = 0
    positions = []
    text = ""
    def __init__(self, text):
        self.text = text
        self.height = (len(self.text.split("\n")))
        self.width = len(max(self.text.split('\n'), key = len))
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