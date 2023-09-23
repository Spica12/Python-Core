class TNum:

    def __init__(self, id):
        self.id = id
        id += 20            # Даний рядок нічого не вирішує для id


obj = TNum(1)
print(obj.id)       # 1