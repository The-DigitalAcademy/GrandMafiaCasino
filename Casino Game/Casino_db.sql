-- Active: 1668349128230@@127.0.0.1@5430@mafia_casino_db
DROP TABLE IF EXISTS details,casino_account,user_login;
CREATE TABLE user_login(
user_id SERIAL PRIMARY KEY NOT NULL,
username VARCHAR(25) UNIQUE NOT NULL,
password VARCHAR(25) NOT NULL
);

CREATE TABLE casino_account(
user_id SERIAL,
Balance INT NOT NULL,
Account_number INT NOT NULL,
CONSTRAINT fk_casino_acc
    FOREIGN KEY(user_id) 
    REFERENCES user_login(user_id)
    ON DELETE CASCADE
);

CREATE TABLE details(
user_id SERIAL ,
phone VARCHAR(10) NOT NULL,
email VARCHAR(25) NOT NULL,
address VARCHAR(50) NOT NULL,
CONSTRAINT fk_details
    FOREIGN KEY(user_id) 
    REFERENCES user_login(user_id)
    ON DELETE CASCADE
);

INSERT INTO user_login(username, password)
VALUES
('Mpho', 'fhgfjk2'),
('Neo', 'sjajhdfj')
;

INSERT INTO casino_account(balance,account_number)
VALUES
(2000,001),
(1000,002)
;

INSERT INTO details(phone, email, address)
VALUES
('0872321414','mpho@gmail.com','56 mooi'),
('0765432367','neo@gmail.com','75 pine')
;