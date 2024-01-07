# 建造者模式，学会这个模式到底是如何使用，在什么场景下。

class Builder:
    def create_cpu(self):
        pass
    def create_os(self):
        pass
    def create_internal_storage(self):
        pass
    def create_external_storage(self):
        pass
class Competer:
    def __init__(self,cpu,os,interan_storage,external_storage):
        self.cpu = cpu
        self.os = os
        self.internal_storage = interan_storage
        self.external_storage = external_storage
    def print_computer_configInfo(self):
        print(f'cpu is {self.cpu}\n os is {self.os} \n internal_storage is {self.internal_storage} \n external_storage is {self.external_storage}')


class BasicCompeterBuilder:
    def create_cpu(self):
        return 'basic cpu'
    def create_os(self):
        return 'basic os'
    def create_internal_storage(self):
       return 'basic internal storage'
    def create_external_storage(self):
       return 'basic external storage'


class Director:
  def create_computer(self,builder):
        os = builder.create_os()
        cpu = builder.create_cpu()
        internal_storage = builder.create_internal_storage()
        external_storage = builder.create_external_storage()
        return Competer(cpu,os,internal_storage,external_storage)


def main():
    pass
if __name__ == '__main__':
    main()

