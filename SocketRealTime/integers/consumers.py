import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asyncio import sleep
import pymysql
from itertools import count
from integers.leer import lectura

class WSConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for i in count(1):
            miConexion = pymysql.connect(host='127.0.0.1', user='Daniel', passwd='Miranda-643092', db='iot2040')
            cur = miConexion.cursor()
            cur.execute("SELECT numero FROM database_numero0 order by id desc limit 1")
            val0 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero1 order by id desc limit 1")
            val1 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero2 order by id desc limit 1")
            val2 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero3 order by id desc limit 1")
            val3 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero4 order by id desc limit 1")
            val4 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero5 order by id desc limit 1")
            val5 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero6 order by id desc limit 1")
            val6 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero7 order by id desc limit 1")
            val7 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero8 order by id desc limit 1")
            val8 = [a[0] for a in cur.fetchall()]
            cur.execute("SELECT numero FROM database_numero9 order by id desc limit 1")
            val9 = [a[0] for a in cur.fetchall()]
            val = [val0, val1, val2, val3, val4, val5, val6, val7, val8, val9]
            await self.send(json.dumps({'message': val}))
            await sleep(0.1)
            imp = ""

            var = lectura(imp)
