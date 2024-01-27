
'''
golang

的子类和父类直接是属于约束关系，强调的是对其他类的对象的组合，没有明确的继承的概念，因为继承是父类和子类的关系，但是golang子类和父类之间并不存在这样的关系。

python 的继承强调的是对父类的方法和变量的调用，从而减少代码冗余，重写代码，实现多态，子类和父类之间并没有约束明确的关系。




所以这里可以整理出三个点：

1.父类和子类之间的接口规范如何实现？如何规定的子类必须要实现的接口。

2.父类和子类之间的接口约束如何实现？ 也就是抽象类的和具体类之间的接口约束是如何实现？ 如何规定了传入的子类必须要继承父类。

但是对于像继承了父类的子类而言，都可以当父类使用，对于任何期望传入父类的地方，都可以传入继承了该父类的子类。从而实现多态性。

只有静下心来，考虑清楚事情的本质才能做好每件事情。
'''


class PhoneFactory:
    def create_phone(self):
        pass

class XiaoMiFactory(PhoneFactory):
    def create_phone(self):
       return XiaoMi()

class IphoneFactory(PhoneFactory):

    def create_phone(self):
        return Iphone()

class Cpu:
    def get_cpu_manufacturer(self):
        pass
class Os:
    def get_operator_system(self):
        pass

class IntelCpu(Cpu):
    def get_cpu_manufacturer(self):
        return 'CPU provided by Intel.'

class GenCpu(Cpu):
    def get_cpu_manufacturer(self):
        return 'CPU provided by Gen.'

class Android(Os):
    def get_operator_system(self):
        return 'Android'

class Ios(Os):
    def get_operator_system(self):
        return 'Ios'

class Phone:
    def get_phoneInfo(self):
        pass
class XiaoMi(Phone):
    def get_phoneInfo(self):
        return Android(),IntelCpu()


class Iphone(Phone):
   def get_phoneInfo(self):
       return Ios(),GenCpu()

def main():
   create_phone(IphoneFactory())
   create_phone(XiaoMiFactory())

def get_AllInfo(Phone):
    os,cpu = Phone.get_phoneInfo()
    print(os.get_operator_system())
    print(cpu.get_cpu_manufacturer())

def create_phone(PhoneFactory):
    phone = PhoneFactory.create_phone()
    get_AllInfo(phone)

if __name__ == '__main__':
    main()
