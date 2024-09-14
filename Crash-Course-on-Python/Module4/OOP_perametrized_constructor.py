class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)