
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