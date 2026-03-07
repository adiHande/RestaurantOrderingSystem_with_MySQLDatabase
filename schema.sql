CREATE DATABASE IF NOT EXISTS restaurant_system;
USE restaurant_system;

-- Orders Table -- One row per receipt 

-- Order Items Table--  Multiple rows per receipt 

CREATE TABLE IF NOT EXISTS orders(
    order_id int auto_increment primary key,
    order_time timestamp default current_timestamp,
    subtotal decimal(10,2) not null,
    tax decimal(10,2) not null,
    tip decimal(10,2) not null,
    total decimal(10,2) not null,
    signature varchar(50) 
);

ALTERTABLE orders AUTO_INCREMENT = 200;  

CREATE TABLE IF NOT EXISTS order_items(
    item_id int auto_increment primary key,
    order_id int not null,
    item_name varchar(100) not null,
    quantity int not null,
    price decimal(10,2) not null,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
)

