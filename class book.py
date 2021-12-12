class book:
    def __init__(self, title, author,price):
        self.title=title
        self.author=author
        self.price=price

    def View(self):
        print(self.title, self.author,  self.price,'Rs')

b1=book('Hello', 'CD Patel', 310)

b1.View()