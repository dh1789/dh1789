#!/usr/bin/env python3
# -- Content-Encoding: UTF-8 --


#1. 기능명 입력 받음
#2. 조건 입력(1개 이상)
#3. 결과 확인(1개 이상)
#- 1개 이상일 경우 성공 조건 입력(모두 성공, 1개이상 성공)
#4. 테스트 확인 가능
#5. 테스트 실행 가능
#6. 실행 결과 확인 가능(에러 포함)

class scenario(object):
   def __init__(self):
      self._title = ''
      self._given = []
      self._when = []
      self._then = []

   def get_info(self):
      print("title : {}".format(self._title))
      print("given : {}".format(self._given))
      print("when : {}".format(self._when))
      print("then : {}".format(self._then))

   def set_title(self, title):
      self._title = title

   def add_given(self,given):
      self._given.append(given)

   def add_whan(self,when):
      self._when.append(when)

   def add_then(self,then):
      self._then.append(then)

   def run(self):
       for given in self._given:
          if given.run() == False:
             pass

       for when in self._when:
          if when.run() == False:
             pass

       for then in self._then:
          if then.run() == False:
             pass


class obj_given(object):
   def __init__(self):
      self._title = ''
      self._plugin = None
      self._argument = None

   def set_title(self, title):
      self._title = title

   def set_plugin(self,plugin):
      self._plugin = plugin

   def set_argument(self,argument):
      self._argument = argument

   def run(self):
      self._plugin.run(self._plugin, self._argument)

class obj_plugin(object):
   def __init__(self):
       pass

import pymysql

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



a = scenario()

#a.set_title('호스트명 변경')
#a.add_given('호스트명 aaa가 주어졌을 때 ')
#a.add_whan('호스트명을 bbb로 바꾸면')
#a.add_then('호스트명은 bbb로 바뀌여져 있어야 한다')

set_password = obj_given()
set_password.set_plugin(plugin_mysql)
set_password.set_argument({
   'host':'172.16.10.181',
   'user':'ipplus',
   'passwd':'smartnac01',
   'db':'DBN_IPPlus',
   'charset':'latin1',
   'query':'select * from T_AgentInfo',
})


a.add_given(set_password)


a.run()

#b = plugin_mysql()
#b.run()
