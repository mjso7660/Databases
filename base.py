'''
Author: Min Joon So
Course: ECE 464 DB
HW #1. Part 2

Brief description:
    
I used sqlalchemy to implement ORM and implemented the exact same queries from part 1.\
How I wrote tests is I use assert to compare two results: one from engine.execute(<mysql query>) which \
returns basically a list of tuples, each tuple being a row. The other result I am comparing to is \
queries I got from using sqlalchemy ORM using session.query(). Since they are instances of their own\
object classes, I loaded the contents (tuples) into two lists and compare the lists if they are the same.
'''

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import create_engine, exists, Table, func, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Integer, String, Date, distinct, not_
import pytest

# environment variable depending on the user
USERNAME = ''
PASSWORD = ''
DATABASE = 'sailors2'

# declare, run engine for .execute(<mysql command>) queries
engine = create_engine('mysql://'+USERNAME+':'+PASSWORD+'@localhost')
engine.connect()
engine.execute("use sailors2")

# declare engine for orm sqlalchemy query
engine2 = create_engine('mysql://'+USERNAME+':'+PASSWORD+'@localhost')
engine2.connect()
engine2.execute("use sailors2")
Session = sessionmaker(bind=engine2)
Base = declarative_base()

class Boats(Base):
    __tablename__ = 'boats'
    
    bid = Column(Integer, primary_key = True)
    bname = Column(String)
    color = Column(String)
    length = Column(Integer)
    
    def __init__(self,bname, color, length):
        self.bname = bname
        self.color = color
        self.length = length
        
        
class Sailors(Base):
    __tablename__ = 'sailors'
    
    sid = Column(Integer, primary_key = True)
    sname = Column(String)
    rating = Column(Integer)
    age = Column(Integer)
    
    def __init__(self,sname, rating, age):
        self.sname = sname
        self.rating = rating
        self.age = age

class Reserves(Base):
    __tablename__ = 'reserves'
    
    sid= Column(Integer,ForeignKey('sailors.sid'),primary_key = True)
    bid= Column(Integer,ForeignKey('boats.bid'),primary_key = True)
    day = Column(Date, primary_key = True)

# declare session for test cases
session = Session()

def is_identical(mysql_cmd, orm_query):
    '''
    mysql_cmd[string]: mysql query command in string
    orm_query[sqlalchemy.result]: the result of running orm query
    ---
    Compares the result of two queries, one by running 'engine.execute(<mysql query>)' and the other by running\
    sqlalchemy.session.query() 
    ---
    return: if the two results are identical or not
    
    '''
    mysql_list = []
    orm_list = []
    mysql_result = engine.execute(mysql_cmd)
    for x in mysql_result:
        mysql_list.append(x)
    for y in orm_query:
        orm_list.append(y)
    return mysql_list == orm_list

def run_test():
    '''
    testing problem 1 - 7 using assertions
    '''
    #1
    q11 = session.query(func.count('*')).filter(Reserves.bid == Boats.bid).group_by(Reserves.sid)
    q12 = session.query(distinct(Boats.bname), Sailors.sname,func.count('*')).outerjoin(Reserves).filter(Boats.bid==Reserves.bid).outerjoin(Sailors).filter(Sailors.sid==Reserves.sid).group_by(Boats.bid, Boats.bname, Sailors.sid, Sailors.sname).order_by(Boats.bname).order_by(Sailors.sname)#.having(func.count('*')>=all(q1))
    #2
    q21 = session.query(Boats).join(Reserves).filter(Reserves.bid == Boats.bid).subquery()
    q22 = session.query(q21.c.bid, q21.c.bname, func.count('*')).group_by(q21.c.bid)
    assert is_identical('select bid, bname, count(*) as c from (select * from reserves left join boats using(bid)) as kk where not bid=0 group by bid',q22)
    #3
    q31 = session.query(Boats.bid).filter(Boats.color=='red')
    q32 = session.query(Reserves.sid).filter(Reserves.bid==all(q31))
    q33 = session.query(Sailors.sname).filter(Sailors.sid.in_(q32))
    assert is_identical("select s.sname from sailors s where s.sid in (select r.sid from reserves r where r.bid = all(select b.bid from boats b where b.color = 'red'))",q33)
    #4
    q41 = session.query(distinct(Reserves.sid)).outerjoin(Boats).filter(Boats.color!='red')
    q42 = session.query(distinct(Reserves.sid)).filter(Reserves.sid.notin_(q41))
    q43 = session.query(Sailors.sid,Sailors.sname,Sailors.rating, Sailors.age).filter(Sailors.sid.in_(q42))
    assert is_identical("select * from sailors s where s.sid in(select distinct r.sid from reserves r where r.sid not in (select distinct r.sid from reserves r left join boats b on r.bid = b.bid where b.color !='red'))",q43)
    #5
    q5 = session.query(Reserves.bid,func.count('*').label('c')).group_by(Reserves.bid).order_by(desc('c')).limit(1)
    assert is_identical("select bid, res.c from (select bid, count(*) as c from reserves group by bid order by c desc limit 1) as res",q5)
    #6
    subquery = session.query(Boats.bid).filter(Boats.color=="red")
    query = session.query(Reserves.sid).filter(Reserves.bid.in_(subquery))
    query2 = session.query(Sailors.sname).filter(Sailors.sid.notin_(query))
    assert is_identical("select s.sname from sailors s where s.sid not in (select r.sid from reserves r where r.bid in (select b.bid from boats b where b.color = 'red'))",query2)
    #7
    sailors = session.query(func.avg(Sailors.age)).filter(Sailors.rating==10)
    assert is_identical("select avg (s.age) from sailors s where s.rating = 10",sailors)
    
if __name__ == '__main__':
    run_test()
