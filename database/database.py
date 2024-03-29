import redis



#

class DBWrapper:
    def __init__(self) -> None:
        pass


def build_redis_connection()->redis.Redis:
    return redis.StrictRedis(host='localhost', port=6379, db=0,decode_responses=True)



def testGenerateConteents(db:redis.Redis):
    import time
    import random
    #Generate Two Devices
    
    devices = ["Device1", "Device2"]
    startTime = time.time()
    
    while time.time() < startTime+10:
        device = devices[random.randint(0,1)]
        info = random.random()*100
        currentTime = time.time()
        
        db.rpush(device+":"+"Temperature", str(info)+":"+str(currentTime))

# testGenerateConteents(db)


def getTestData()->list:
    db = build_redis_connection('localhost', 6379, 0)
    info1 =db.lrange("Device1:Temperature", 0, -1)
    info2 = db.lrange("Device2:Temperature", 0, -1)
    return [info1, info2]

# 