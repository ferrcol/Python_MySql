from mysql.connector import pooling
from mysql.connector import Error

class Conection:
    DATABASE = "gym_db"
    USERNAME = "root"
    PASSWORD = "1234"
    DB_PORT = "3306"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "gym_pool"
    pool = None

    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f"Error to get pool: {e}")
        else:
            return cls.pool
        
    @classmethod    
    def get_conection(cls):
        return cls.get_pool().get_connection()
    
    @classmethod
    def release_conection(cls, conection):
        conection.close()

if __name__ == "__main__":
    pool = Conection.get_pool()
    print(pool)
    conection1 = pool.get_connection()
    print(conection1)
    Conection.release_conection(conection1)
    print("realease conection1")