from nonebot import on_command, CommandSession
import json
import requests
import time

@on_command('fans_search', aliases = ('粉丝'))
async def fans_search(session:CommandSession):
    url = 'https://api.bilibili.com/x/relation/stat?vmid=259333'
    response = requests.get(url=url)
    r = json.loads(response.text)
    result = r['data']['follower']
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    await session.send("当前时间："+str(t)+"，咖喱现在的粉丝数："+str(result)+"，还剩"+str(1000000-result)+"到百万")