# For implement
from sql_connection import get_sql_connection

# For test
# from backend.sql_connection import get_sql_connection

from datetime import datetime

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("SELECT p.product_id, p.name, p.uom_id, p.price_per_unit, u.uom_name from products p inner join uom u on p.uom_id = u.uom_id")

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )
    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid
    # return product_id

# edit
def update_product(connection, product):
    cursor = connection.cursor()
    query = ("UPDATE products SET name=%s, uom_id=%s, price_per_unit=%s WHERE product_id=%s")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'], product['product_id'])
    cursor.execute(query, data)
    connection.commit()
    return True



if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
    # print(insert_new_product(connection, {
    #     'product_name': 'chips',
    #     'uom_id': '1',
    #     'price_per_unit': 10
    # }))