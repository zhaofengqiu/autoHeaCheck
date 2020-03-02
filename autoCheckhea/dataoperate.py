import requests
import json
import time
from exts import db,app
from utils import write,post
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine
from config import SMTPPASSWD,FROMADDR,SQLALCHEMY_DATABASE_URI


Base = declarative_base()
class Info(Base):
    __tablename__ = "info"
    name =  Column( String(20))
    sex =  Column( String(2))
    schoolnum = Column( String(20), primary_key=True)
    bumen = Column( String(100))
    phone =  Column( String(20))
    email = Column( String(40))
    def to_dict(self):
        user_dict = {
            "name": self.name,
            "sex": self.sex,
            "schoolnum": self.schoolnum,
            "bumen": self.bumen,
            "phone": self.phone,
            "email":self.email
        }
        return user_dict
class DataOperate():
    def __init__(self):
        self.userlist=[]
        self.init_table()
        self.init_userlist()
    def init_table(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    def init_userlist(self):
        try:
            ans = self.session.query(Info).all()
        except Exception as ce:
            Base.metadata.create_all(self.engine)
            ans = self.session.query(Info).all()
        for an in ans:
            self.userlist.append(an.to_dict())

    def send_req(self):

        url = "https://lightapp.wzu.edu.cn/api/questionnaire/questionnaire/addMyAnswer"
        headers = {
            "Origin": "https://lightapp.wzu.edu.cn",
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; M6 Note Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.110 Mobile Safari/537.36 weishao(6.5.3.72535) wsi18n(zh)",
            "Referer": "https://lightapp.wzu.edu.cn/questionnaire/addanswer?page_from=onpublic&activityid=2148&can_repeat=1",
            "X-Requested-With": "cn.edu.wzu.wsnew",
            "Content-Type": "application/json;charset=UTF-8",
        }
        with open('static/data.txt', 'r', encoding='utf-8') as f:
            json_data = f.read()
        for user_data in self.userlist:
            find_data = json_data
            for key,value in user_data.items():
                if value is not None:
                    find_data = find_data.replace('{'+key+'}',value)

            msg = requests.post(url=url, headers=headers, json=json.loads(find_data)).text
            msg=time.asctime( time.localtime(time.time()) )+" "+str(user_data.get('name')+" ")+msg+"\n"
            print(msg)
            self.send_email(msg,user_data.get('email'))

    def send_email(self,msg,sender):
        if sender is None:
            return
        emailText = write(msg,FROMADDR,sender)
        post(emailText,FROMADDR,sender,SMTPPASSWD)
da_op = DataOperate()
da_op.send_req()
