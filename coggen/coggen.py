from redis import Redis
from rq import SimpleWorker, Queue


def queenbee(redisServer, task, *args):
    print("the TASK is %s" % task)

    queue = Queue(connection=Redis.from_url(redisServer))
    queue.enqueue(task, args, timeout=1800)


def mainsub():
    #url='redis://dockerplay'
    url='redis://172.31.3.145'
    
    workFile='workIn.txt'

    with open(workFile) as f:
        for line in f:
            print (line)
            a = line.split('h03v03/')
            id = 'h03v03/' + a[1]
            print (id)
            queenbee(url, 'buntarDedup.bunde', id ,)

if __name__ == "__main__":
    mainsub()

