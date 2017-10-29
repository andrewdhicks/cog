from redis import Redis
from rq import SimpleWorker, Queue

import argparse


def bullshit():
    print("BULSHIT Walks!")

def workerbee(task):
    print("the TASK is %s" % task)

    queue = Queue(connection=Redis())
    queue.enqueue('time.sleep',5)
    worker = SimpleWorker([queue], connection=queue.connection)
    worker.work(burst=True)  # Runs enqueued job
    # Check for result...
    queue.enqueue(bullshit)
    worker = SimpleWorker([queue], connection=queue.connection)
    worker.work(burst=True)  # Runs enqueued job


def mainsub():
    #workerbee(task='builddir l7xxx')
    parser = argparse.ArgumentParser(description='Test RQ by sending some work python subs')
    parser.add_argument('url', metavar='URL', type=string, nargs='+',
                    help='the url for the redis server ')

    args = parser.parse_args()
    print (args.url)

if __name__ == "__main__":
    mainsub()


