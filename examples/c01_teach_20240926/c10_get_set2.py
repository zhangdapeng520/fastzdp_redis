import fastzdp_redis as fzr
import time

# 建立链接
r = fzr.FastZDPRedisClient()

r.set("name", "张大鹏")
print(r.get("name"))


r.set("name", "张大鹏", 3)
time.sleep(3)
print(r.get("name"))
