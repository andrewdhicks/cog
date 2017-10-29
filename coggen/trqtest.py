from redis import Redis
from rq import SimpleWorker, Queue

def bullshit():
    print("BULLSHIT Walks!")

def workerbee(task):
    print("the TASK is %s" % task)

    queue = Queue(connection=Redis())
    queue.enqueue('time.sleep',5)
    #worker = SimpleWorker([queue], connection=queue.connection)
    #worker.work(burst=True)  # Runs enqueued job
    # Check for result...
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)
    queue.enqueue(bullshit)
    #worker = SimpleWorker([queue], connection=queue.connection)
    #worker.work(burst=True)  # Runs enqueued job


def mainsub():
    workerbee(task='builddir l7xxx')

if __name__ == "__main__":
    mainsub()


