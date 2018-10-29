from sqlalchemy.schema import Column, ForeignKey
#from sqlalcehmy.types import integer, String
from sqlalchemy import create_engine, exists, Table, func, desc, Integer, String, Date, distinct, not_, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, aliased

import time
import pytest

# environment variable depending on the user
USERNAME = ''
PASSWORD = ''
DATABASE = 'sailors2'

# run engine
engine = create_engine('mysql://'+USERNAME+':'+PASSWORD+'@localhost')
engine.connect()
engine.execute('use '+DATABASE)

#run session
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

class Boats(Base):
    '''
    new attributes:
        wear [int]: (1-100)% of how much a boat is worn oout
        rent [int]: $$ of how much rent rate is for a obat
    '''    
    __tablename__ = 'boats'
    
    bid = Column(Integer, primary_key = True)
    eid = Column(Integer)
    bname = Column(String)
    color = Column(String)
    length = Column(Integer)
    wear = Column(Integer) # out of 100%
    rent = Column(Integer)
    
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
    '''
    new attributes:
        start_d [date]: start date of rent
        return_d [date]: return date of rent
    '''
    __tablename__ = 'reserves'
    
    sid= Column(Integer,ForeignKey('sailors.sid'),primary_key = True)
    bid= Column(Integer,ForeignKey('boats.bid'),primary_key = True)
    day = Column(Date, primary_key = True)
    start_d = Column(Date)
    return_d = Column(Date)

class employees(Base):
    '''
    new class which describes employees of the shop
        eid[int]: primary key
        ename[string]: name of employee
        salary[int]: montly salary rate
        employement_duration[int]: # of years worked for the shop
    '''
    __tablename__ = 'employees'
    
    eid = Column(Integer, primary_key = True)
    ename = Column(String)
    salary = Column(Integer)
    employment_duration = Column(Integer)

def repair_tracker():
    '''
    prints out boats with wear < 30%
    ---
    Equivalent to <Select * from Boats where Boats.wear > 70>
    '''
#    session = Session()
    print('-----Repair Tracker-----')
    wear_boats = session.query(Boats).filter(Boats.wear>70).all()
    for each in wear_boats:
        print('Boat name "{}" with id "{}" has "{}"% wear-out: needs repair'.format(each.bname, each.bid, each.wear))
    return wear_boats

def monthly_account():
    '''
    prints out how much each sailor should pay depending
        - (1) how many days a sailor is borrowing a boat
        - (2) boat rent fee
        - (3) sum of (1)*(2)
    ---
    Equivalent to <Select s.sname, s.sid, result.payment from sailors s, (select r.sid, sum b.rent*datediff(r.return_d,r.start_day from boats b, reserves r where b.bid = r.bid group by r.sid)>
    '''
#    session = Session()
    print('-----Monthly Payment-----')
    payment1 = session.query(Reserves.sid.label('sid'), func.sum(Boats.rent*func.datediff(Reserves.return_d,Reserves.start_d)).label('payment')).filter(Boats.bid==Reserves.bid).group_by(Reserves.sid).subquery()
    payment = session.query(Sailors.sname, Sailors.sid,payment1.c.payment).filter(Sailors.sid==payment1.c.sid)
    for i in payment:
        print('Sailor "{}" (#{}) owes ${} dollars this month'.format(i.sname,i.sid,i.payment))
    return payment
        
def today(today):
    '''
    prints out all the boats to be rented today
    '''
#    session = Session()    
    day2 = session.query(Reserves).filter(Reserves.start_d == today).subquery()
    day = session.query(Sailors.sname, day2.c.bid).filter(Sailors.sid == day2.c.sid)
    print('-----TODAY-----')
    print('Today, the sailors will borrow the following boats')
    for each in day:
        print('Sailor "{}" / Boat: {}'.format(each.sname, each.bid))
    return day
        
def pay_salary():
    '''
    pay salary to employees based on: 
        - how many boats they are in charge of 
        - salary rate
    ---
    Equivalent to <select employees.ename, employees.salary*pay.sum from employees join (select b.eid, sum(result.c) from boats b join (select bid, count(*) as c from reserves group by bid) as result on b.bid = result.bid group by b.eid as payment) where payment.eid = employees.eid>
    '''
    print('-----Pay Salary-----')    
    sub = session.query(Reserves.bid, func.count('*').label('cnt')).group_by(Reserves.bid).subquery()
    pay = session.query(Boats.eid,func.sum(sub.c.cnt).label('sum')).join(sub).filter(Boats.bid == sub.c.bid).group_by(Boats.eid).subquery()
    person = session.query(employees.ename,employees.salary*pay.c.sum).filter(employees.eid == pay.c.eid)
    for each in person:
        print('employee "{}" should be paid ${} for this month'.format(each.ename, each[1]))
    return sub   

if __name__ =='__main__':
    TODAY_DATE = '1998-12-17'
    repair_tracker()
    monthly_account()
    today(TODAY_DATE)
    pay_salary()
