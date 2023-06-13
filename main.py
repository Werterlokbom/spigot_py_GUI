import mcpi.minecraft as minecraft

# 设置服务器地址和端口
server_address = "localhost"  # 服务器 IP 或 "localhost"
server_port = 4711            # Raspberry Juice 默认端口

# 连接到 Minecraft 服务器
mc = minecraft.Minecraft.create(server_address, server_port)

# 发送消息到 Minecraft 中
mc.postToChat("Hello, Minecraft!")