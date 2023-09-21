DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS comment;

CREATE TABLE user (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_since TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_name VARCHAR(50),
    user_last_name VARCHAR(50),
    is_employee BOOLEAN NOT NULL
);

CREATE TABLE ticket (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_open BOOLEAN,
    content TEXT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE comment (
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content TEXT,
    ticket_id INTEGER NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id)
);