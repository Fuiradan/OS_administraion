import os
import pytest
import app

def test_db_exists():
    app.NewTables()
    check_file = os.path.exists('db/db.db')
    assert check_file == True


def test_db_columns_exist_clients():
    tmp = 'SELECT "t1"."id", "t1"."name", "t1"."city", "t1"."address" FROM "clients" AS "t1"'
    assert tmp == str(app.clients.select())

def test_db_contains_columns_orders():
    tmp = 'SELECT "t1"."id", "t1"."client_id", "t1"."date", "t1"."amount", "t1"."description" FROM "orders" AS "t1"'
    assert str(app.orders.select()) == tmp

def test_db_contains_amount_rows_1():
    app.filling()
    assert len(app.clients.select()) >= 10

def test_db_contains_amount_rows_2():
    app.filling()
    assert len(app.orders.select()) >= 10
    


    