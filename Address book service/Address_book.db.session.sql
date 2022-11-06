-- Active: 1667747711399@@127.0.0.1@5430@address_book_db
CREATE TABLE details(
    id SERIAL PRIMARY KEY NOT NULL,
    names VARCHAR(50) NOT NULL,
    email VARCHAR(25) NOT NULL,
    address VARCHAR(45) NOT NULL,
    contact VARCHAR(10) NOT NULL
);

INSERT INTO details(names, email, address, contact )
VALUES
('John Diale','john@gmail.com','22Top','0684214968'),
('Mbedzi Gudani','mbedzigudani@gmail.com', '111 kerk', '0718345255');