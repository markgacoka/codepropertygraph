import pyorient

class Server:
    def __init__(self, user, password, dbName):
        self.user = user
        self.password = password
        self.dbName = dbName
        self.host='127.0.0.1'
        self.port=2424
        self.dbType=pyorient.DB_TYPE_GRAPH
        self.storageType=pyorient.STORAGE_TYPE_MEMORY
        
    @property
    def serverVersion(self):
        if self.client and self.client.version:
            version = self.client.version
            return version.major, version.minor, version.build

    def run_pyorient_server(self):
        try:
            self.client = pyorient.OrientDB(host=self.host, port=self.port)
            self.session_id = self.client.connect(self.user, self.password)
        except pyorient.exceptions.PyOrientConnectionException:
            print("OrientDB connection failed. Check if DB is running on port {}".format(self.port))
        if not self.client.db_exists(self.dbName, self.storageType):
            self.createDb(self.dbName, self.dbType, self.storageType)
        self.client.db_open(self.dbName, self.user, self.password)
        if not (self.serverVersion and self.serverVersion[0] >= 2 and self.serverVersion[1] >= 2):
            print("OrientDB version should be atleast 2.2. Current version is {}".format(".".join(map(str, self.serverVersion))))
        
example_server = Server(user='admin', password='admin', dbName='demodb')
example_server.run_pyorient_server()
