class Server:
    def __init__(self,serverId,ipAddress):
        self.serverId=serverId
        self.ipAddress=ipAddress

    def start(self,status,memory_usage):
        self.status=status
        self.memory_usage=memory_usage
        print(f'Server is started with {self.ipAddress}')
        print(f'Status : {self.status}')

    def stop(self,status,memory_usage):
        self.status=status
        self.memory_usage=memory_usage
        print(f'Server is stop with {self.ipAddress}')
        print(f'Status : {self.status}')

    def restart(self):
        self.stop('OFFLINE','NO')
        self.start('ONLINE','YES')
        print(f'Server is restarted with {self.serverId}')
        
    

server1= Server('1010','19.10.20.230.34');
server1.start('ONLINE','YES')
server1.stop('OFFLINE','NO')
server1.restart()
server2= Server('2020','20.80.80.500.344');
