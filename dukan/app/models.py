"""
Definition of models.
"""

from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
# Create your models here.
import sqlite3

class Database:
    def __init__(self, name):
        self._conn = sqlite3.connect(name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
class register(models.Model):
    """Not using this."""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    shop_name = models.CharField(max_length=20)
    contact = models.IntegerField(default=1)
    store_type = models.CharField(max_length=20)
    shop_no = models.IntegerField(default=1)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    pincode = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
