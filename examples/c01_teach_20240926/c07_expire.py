import redis
import time

# 建立链接
# decode_responses=True 得加在获取连接池对象的参数里面, 否则不生效
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# 设置key
# ex 秒
# px 毫秒
r.set('foo', 'bar', ex=3)

# 获取key的值
print(r.get('foo'))


time.sleep(3)

print(r.get('foo'))
