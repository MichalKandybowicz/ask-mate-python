from connection import connection_handler
import datetime
from data_manager import dm_general


@connection_handler
def get_users(cursor):
    cursor.execute("""
                    SELECT * FROM users
                    """)
    users = cursor.fetchall()
    return users


@connection_handler
def get_users_sorted(cursor, order_by, order_direction):
    cursor.execute(f"""
                    SELECT * FROM users ORDER BY {order_by} {order_direction}
                    """)
    users = cursor.fetchall()
    return users