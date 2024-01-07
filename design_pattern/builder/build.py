# 建造者模式，学会这个模式到底是如何使用，在什么场景下。
from abc import abstractmethod

class Builder:
    @abstractmethod
    def create_cpu(self):
        pass
    @abstractmethod
    def create_os(self):
        pass
    @abstractmethod
    def create_internal_storage(self):
        pass
    def create_external_storage(self):
        pass
    def create_screen(self):
        pass

class Competer:
    def __init__(self,cpu,os,interan_storage,external_storage):
        self.cpu = cpu
        self.os = os
        self.internal_storage = interan_storage
        self.external_storage = external_storage
    def __str__(self):
        return f'cpu is {self.cpu};os is {self.os}; internal_storage is {self.internal_storage};external_storage is {self.external_storage}'
    def print_computer_configInfo(self):
        print(f'cpu is {self.cpu}\nos is {self.os} \ninternal_storage is {self.internal_storage} \nexternal_storage is {self.external_storage}')




class BasicCompeterBuilder(Builder):
    def create_cpu(self):
        return 'basic cpu'
    def create_os(self):
        return 'basic os'
    def create_internal_storage(self):
       return 'basic internal storage'
    def create_external_storage(self):
       return 'basic external storage'


class ProCompeterBuilder(Builder):
    def create_cpu(self):
        return 'pro cpu'
    def create_os(self):
        return 'pro os'
    def create_internal_storage(self):
        return 'pro internal storage'
    def create_external_storage(self):
        return 'pro external storage'
class Director:

    def __init__(self, builder):
        self.builder = builder

    def create_computer(self):
        os = self.builder.create_os()
        cpu = self.builder.create_cpu()
        internal_storage = self.builder.create_internal_storage()
        external_storage = self.builder.create_external_storage()
        return Competer(cpu, os, internal_storage, external_storage)
    def create_computer_with_screen(self):
        pass


def main():
    director1 = Director(BasicCompeterBuilder())
    computer = director1.create_computer()
    computer.print_computer_configInfo()
    print('')
    director2 = Director(ProCompeterBuilder())
    computer = director2.create_computer()
    computer.print_computer_configInfo()
    print('')
    print(computer)

if __name__ == '__main__':
    main()

