# 定义抽象处理者
class Approver:
    def __init__(self, name, approval_limit, successor=None):
        self.name = name
        self.approval_limit = approval_limit
        self.successor = successor

    def process_request(self, request_amount):
        if request_amount <= self.approval_limit:
            print(f"{self.name} approved the request.")
        elif self.successor:
            print(f"{self.name} cannot approve. Passing to {self.successor.name}.")
            self.successor.process_request(request_amount)
        else:
            print(f"{self.name} cannot approve. Request exceeds all approval limits.")

# 具体处理者
manager = Approver("Manager", 1000)
director = Approver("Director", 5000)
vp = Approver("VP", 10000)

# 设置责任链
manager.successor = director
director.successor = vp

# 客户端代码
if __name__ == "__main__":
    # 创建报销申请
    request_amount = 8000

    # 提交请求给责任链的起始点
    manager.process_request(request_amount)
