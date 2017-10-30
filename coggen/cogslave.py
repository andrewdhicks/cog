from redis import Redis
from rq import Worker, SimpleWorker, Queue

def bullshit(msg):
   line = '---'*40
   print(line)
   print("Hey CHERYL this is bullshit from cogslave!\n")
   print(msg)
   print(line)

def workerbee(redisServer):

    queue = Queue(connection=Redis.from_url(redisServer))
    worker = SimpleWorker([queue], connection=queue.connection)
    worker.work()


def mainsub():
    url='redis://dockerplay'
    workerbee(redisServer=url)

if __name__ == "__main__":
    mainsub()

