from redis import Redis
from rq import SimpleWorker, Queue

import argparse


def bullshit():
    print("BULSHIT Walks!")

def workerbee(redisServer, task):
    print("the TASK is %s" % task)

    queue = Queue(connection=Redis.from_url(redisServer))
    queue.enqueue('time.sleep',5)
    # Check for result...
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)


def mainsub():
    parser = argparse.ArgumentParser(description='Test RQ by sending some work python subs')
    parser.add_argument('url', help='the url for the redis server ')

    args = parser.parse_args()
    print (args.url)
    workerbee(redisServer=args.url, task='builddir l7xxx')

if __name__ == "__main__":
    mainsub()

