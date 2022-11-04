CREATE TABLE address_book(
    id SERIAL PRIMARY KEY NOT NULL,
    names VARCHAR(50) NOT NULL,
    email VARCHAR(25) NOT NULL,
    address VARCHAR(45) NOT NULL,
    contact VARCHAR(10) UNIQUE NOT NULL
);

INSERT INTO address_book(names, email, address, contact )
VALUES('Mbedzi''Gudani','mbedzigudani@gmail.com', '111 kerk', '0718345255')

RETURNING*