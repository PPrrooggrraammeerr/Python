DROP DATABASE IF EXISTS invoices;

CREATE DATABASE IF NOT EXISTS invoices;

USE invoices;

CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(50) NOT NULL,
    invoice_date DATE NOT NULL,
    file_name VARCHAR(255),
    status VARCHAR(50)
);
