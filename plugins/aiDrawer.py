# -*- coding: utf-8 -*-
import asyncio
from io import BytesIO

import httpx

import requests
from PIL import Image

from plugins.RandomStr import random_str


async def draw(prompt,path= "./test.png"):
    url=f"https://api.lolimi.cn/API/AI/sd.php?msg={prompt}&mode=动漫"

    async with httpx.AsyncClient(timeout=40) as client:
        r = await client.get(url)
        with open(path,"wb") as f:
            f.write(r.content)
        # print(path)
        return path
async def airedraw(prompt,url,path="./redraw.png"):
    url=f"https://api.lolimi.cn/API/AI/isd.php?msg={prompt}&img={url}&mode=动漫"
    async with httpx.AsyncClient(timeout=40) as client:
        r = await client.get(url)
        with open(path, "wb") as f:
            f.write(r.content)
        # print(path)
        return path
async def draw1(prompt,path="./test.png"):
    url=f"https://api-collect.idcdun.com/v1/images/generations?prompt={prompt}&n=1&model=dall-e-3&size=1024x1024"
    async with httpx.AsyncClient(timeout=40) as client:
        r = await client.get(url)
        url2=r.json().get("data")[0].get("url")
        async with httpx.AsyncClient(timeout=40) as client:
            r1 = await client.get(url2)
        with open(path, "wb") as f:
            f.write(r1.content)
        # print(path)
        return path
# 运行 Flask 应用
if __name__ == "__main__":
    asyncio.run(draw1("正在吃早饭的二次元少女"))
