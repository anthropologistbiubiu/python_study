


class ConcreteFactoryA:
    def __init__(self):
        self.product = 'Product A'
    def get_prouct_name(self):
        return self.product


class ConcreteFactoryB:
    def __init__(self):
        self.product = 'Product B'
    def get_prouct_name(self):
        return self.product

def main():
    facotryA = ConcreteFactoryA()
    print(facotryA.get_prouct_name())

if __name__ == '__main__':
    main()