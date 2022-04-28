import psycopg2
from dbconfig import config


def product_vendor(id):
    conn = None
    sql="SELECT vendors.vendor_id,vendors.vendor_name FROM vendors inner join vendor_parts on vendor_parts.vendor_id = vendors.vendor_id where vendor_parts.part_id=%s"
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(id,))
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows

def vendor_report(id):
    sql = "SELECT vendors.vendor_id,vendors.vendor_name FROM vendors inner join vendor_parts on vendor_parts.vendor_id = vendors.vendor_id where vendor_parts.part_id=%s order by vendor_id"
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (id,))
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows


def product_report(id):
    sql = "SELECT * FROM parts where part_id=%s"
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (id,))
        rows = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows
