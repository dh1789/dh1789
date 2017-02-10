try:
    import pymysql
except ImportError as e:
    print('got error {!r}, errno is {}'.format(e, e.args[0]))
    exit()


from plugin import *

class plugin_mysql(obj_plugin):
    def __init__(self):
        obj_plugin.__init__()
        self._db = None
        self._query= ''
        self._verify=[]
        self._kwargs={}

    def check_argument(self):
        state = True
        for argument in ['host','user','passwd']:
            if  argument not in self._kwargs:
                state = False
                #            _logging.add('invalid argument: {}'.format(self._kwargs))

        if 'port' not in self._kwargs:
            self._kwargs['port'] = 3306

        if 'charset' not in self._kwargs:
            self._kwargs['charset'] = 'latin1'

        if 'query' in self._kwargs:
            self._query = self._kwargs.pop('query')

        if 'verify' in self._kwargs:
            self._verify.append(self._kwargs.pop('verify'))

        #      if 'db' not in self._kwargs:
        #         self._kwargs['db'] = 'DBN_IPPlus'

        if self._kwargs['charset'] != 'utf-8':
            self._kwargs['use_unicode']=False

        self._kwargs['cursorclass']=pymysql.cursors.DictCursor

        return state


    def execute_query(self,):
        # connect옵션에서 아래와 같이 추가설정
        #   charset='latin1', use_unicode=False
        # 데이터 획득 후 아래와 같이 변환해서 사용
        #   row['Name'].decode('cp949')

        try:
            with self._db.cursor() as cursor:
                cursor = self._db.cursor()
                cursor.execute(self._query)
                for row in cursor.fetchall():
                    #result.append(row)
                    print(row['Name'].decode('cp949'))
                    print(row['Name'].decode('cp949'))

        except pymysql.err.MySQLError as e:
            print('got error {!r}, errno is {}'.format(e, e.args[0]))
            self._db.rollback()

        finally:
            self._db.commit()
            self._db.close()

    def connect_db(self):
        try:
            self._db = pymysql.connect(**self._kwargs)

        except pymysql.err.MySQLError as e:
            print('got error {!r}, errno is {}'.format(e, e.args[0]))
            return False

        return True

        # TODO : SSL접속 되도록 해야 함(현재는 일반 접속 되도록 mysql 에 계정 등록 후 작업해야 함)
        # grant all on *.* to 'ipplus'@'%' identified by 'smartnac01';
        # flush privileges;
        #self.db = pymysql.connect(
        #   host='172.16.10.181',
        #   port=3306,
        #   user='smartnac',
        #   passwd='ipzplusz26y7',
        #   db='DBN_IPPlus',
        #   charset='latin1',
        #   use_unicode=False,
        #   cursorclass=pymysql.cursors.DictCursor,
        #                   #       'cert':'/Users/dh1789/PycharmProjects/dh1789/certs/mysql/smartnac.dbms.server.crt',
        #                          'ca':'/Users/dh1789/PycharmProjects/dh1789/certs/mysql/smartnac.dbms.server.ca.crt',
        #                     }
        #)

    def get_server_info(self):
        print(self._db.get_server_info())
        print(self._db.get_host_info())


    def verify(self):
        for item in self._verify:
            # 결과 count 체크
            item['action']

        return True


    def run(self, kwargs):
        self._kwargs = kwargs
        if self.check_argument(self) == False:
            return False

        if self.connect_db(self) == False:
            return False

        if self.execute_query(self) == False:
            return False

        if self.verify(self) == False:
            return False

        return True
