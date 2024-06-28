# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
#     http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import uwebsocket
import _thread


def recv(cli):
    while True:
        # 死循环接收数据
        recv_data = cli.recv()
        print("recv_data = {}".format(recv_data))
        if not recv_data:
            # 服务器关闭连接或客户端关闭连接
            print("cli close")
            client.close()
            break


# 创建客户端, debug=True输出日志, ip和端口需要自己填写, 或者是域名
client = uwebsocket.Client.connect('ws://xxx/', debug=True)

# 线程接收数据
_thread.start_new_thread(recv, (client,))

# 发送数据
client.send("this is a test msg")