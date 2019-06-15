リレーショナルマッピングの仕方
------------------------------

📖 https://momijiame.tumblr.com/post/27327972441/python-%E3%81%AE-or%E3%83%9E%E3%83%83%E3%83%91%E3%83%BC-sqlalchemy-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E3%83%AA%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%8A%E3%83%AB%E3%83%9E%E3%83%83%E3%83%94%E3%83%B3%E3%82%B0%E5%9F%BA%E6%9C%AC-4
📖 https://poyo.hatenablog.jp/entry/2017/01/08/212227#backref%E3%81%AE%E5%A0%B4%E5%90%88

### One to Many

```python
class One(Base):
    __tablename__ = 'one_t'
    id = Column(Integer, primary_key=True)

    manys = relation('Many', uselist=True, back_populates='one')

class Many(Base):
    __tablename__ = 'many_t'
    id = Column(Integer, primary_key=True)
    fid = Column(Integer, ForeignKey('one_t.id'))

    one = relation('One', uselist=False, back_populates='manys')
```

### Many to One

```python
class Many(Base):
    __tablename__ = 'many_t'
    id = Column(Integer, primary_key=True)
    fid = Column(Integer, ForeignKey('one_t.id'))

    one = relation('One', uselist=False, back_populates='manys')

class One(Base):
    __tablename__ = 'one_t'
    id = Column(Integer, primary_key=True)

    manys = relation('Many', uselist=True, back_populates='one')
```

### One to One

```python
class One(Base):
    __tablename__ = 'one_t'
    id = Column(Integer, primary_key=True)

    another_one = relation('AnotherOne', uselist=False, back_populates='one')

class AnotherOne(Base):
    __tablename__ = 'another_one_t'
    id = Column(Integer, ForeignKey('one_t.id'), primary_key=True)

    one = relation('One', uselist=False, back_populates='another_one')
```

### Many to Many

```python
cross_table = Table('many_another_many', Base.metadata,
    Column('many_id', Integer, ForeignKey('many_t.id')),
    Column('another_many_id', Integer, ForeignKey('another_many_t.id'))
)

class Many(Base):
    __tablename__ = 'many_t'
    id = Column(Integer, primary_key=True)

    another_manys = relation('AnotherMany', uselist=True, back_populates='manys', secondary=cross_table)

class AnotherMany(Base):
    __tablename__ = 'another_many_t'
    id = Column(Integer, primary_key=True)

    manys = relation('Many', uselist=True, back_populates='another_manys', secondary=cross_table)
```

### 結合条件を複数定義したいとき

複数のキーとjoinしたり、外部キーと結合する列が一意に定まらないときに`primaryjoin`を使う。

```python
class One(Base):
    __tablename__ = 'one_t'
    id = Column(Integer, ForeignKey('another_one_t.id'), primary_key=True)

    another_one = relation(
        'AnotherOne',
        uselist=False,
        primaryjoin="and_(AnotherOne.id==One.id,"
        "AnotherOne.type=='man')",)

class AnotherOne(Base):
    __tablename__ = 'another_one_t'
    id = Column(Integer, primary_key=True)
    type = Column(String, primary_key=True)

    one = relation('One', uselist=False, back_populates='another_one')
```
