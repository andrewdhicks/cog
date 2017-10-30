from redis import Redis
from rq import SimpleWorker, Queue


def queenbee(redisServer, task, *args):
    print("the TASK is %s" % task)

    queue = Queue(connection=Redis.from_url(redisServer))
    queue.enqueue(task, args, timeout=1800)


def mainsub():
    url='redis://dockerplay'
    queenbee(url, 'cogslave.bullshit', ('hi'))
    queenbee(url, 'buntarDedup.bunde', 'h03v03/LC08_CU_003003_20130414_20170713_C01_V01.xml',)
    #queenbee('h03v03/LC08_CU_003003_20130414_20170713_C01_V01.tif', redisServer=url, task='buntarDedup.bunde')

if __name__ == "__main__":
    mainsub()

