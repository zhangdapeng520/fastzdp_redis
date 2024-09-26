import fastzdp_redis as fzr

# 建立链接
rc = fzr.FastZDPRedisClient()
r = rc.get()

r.set("name", "张大鹏")
print(r.get("name"))
