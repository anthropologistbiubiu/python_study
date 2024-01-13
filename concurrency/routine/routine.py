import asyncio

# 创建和使用协程序
async def my_routine():
    print('my_routine')

def main():
  asyncio.run(my_routine())

# 使用多协程并发网络请求

def multi_routine():
    for _ in range (10):
       asyncio.run(my_routine())


# create task 创建多协程来执行

async def routine1(sem):
    with sem:
        await asyncio.sleep(1)
        print(f'routine1')


async def routine2(sem):
    async with sem:
        await asyncio.sleep(1)
        print(f'routine2')

async def task_rutine(sem):
  tasks = [asyncio.create_task(routine2(sem)) for _ in range (10)]
  for task in tasks:
    await task
  await asyncio.sleep(1)
  print(f'task_rutine 执行完毕')

# 如何控制并发协程的数量 semaphore


if __name__ == '__main__':
    sem = asyncio.Semaphore(2)
    asyncio.run(task_rutine(sem))
