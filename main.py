import sys
import json

class routerSyncWorker:
    def __init__(self):
        self.buffer = []
    def append_metric(self, val):
        self.buffer.append(val)
        return len(self.buffer)

if __name__ == '__main__':
    obj = routerSyncWorker()
    print("Worker engine initialized.")