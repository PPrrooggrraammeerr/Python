DROP DATABASE IF EXISTS my_database;

CREATE DATABASE my_database;

USE my_database;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(255),
    date_of_birth VARCHAR(10),
    cpf VARCHAR(14),
    email VARCHAR(255),
    phone VARCHAR(15)
);

CREATE TABLE address (
    id INT PRIMARY KEY AUTO_INCREMENT,
    road VARCHAR(255),
    neighborhood VARCHAR(255),
    city VARCHAR(255),
    uf VARCHAR(2),
    postcode VARCHAR(9)
);

INSERT INTO users (full_name, date_of_birth, cpf, email, phone) VALUES ('full_name', '01/01/2000', '000.000.000-00', 'email@email.com', '(11) 99999-9999');

INSERT INTO address (road, uf) VALUES ('road B', 'SP');

INSERT INTO users (full_name, date_of_birth, cpf, email, phone) VALUES
('João Silva', '1990-04-15', '123.456.789-00', 'joao.silva@example.com', '(11) 91234-5678'),
('Maria Oliveira', '1985-09-22', '987.654.321-00', 'maria.oliveira@example.com', '(21) 99876-5432'),
('Carlos Souza', '1992-11-30', '456.789.123-00', 'carlos.souza@example.com', '(31) 91345-6789'),
('Ana Costa', '1980-03-10', '321.654.987-00', 'ana.costa@example.com', '(41) 92345-6789'),
('Lucas Almeida', '2000-07-25', '654.321.987-00', 'lucas.almeida@example.com', '(51) 93123-4567'),
('Fernanda Santos', '1995-12-05', '987.123.456-00', 'fernanda.santos@example.com', '(61) 91234-7890'),
('Ricardo Lima', '1988-06-18', '123.789.456-00', 'ricardo.lima@example.com', '(71) 92234-5678'),
('Juliana Pereira', '1994-02-28', '321.987.654-00', 'juliana.pereira@example.com', '(81) 91345-6789'),
('Bruno Martins', '1997-08-14', '654.987.321-00', 'bruno.martins@example.com', '(91) 93123-4567'),
('Patricia Rocha', '1982-10-07', '789.654.123-00', 'patricia.rocha@example.com', '(41) 93345-6789');

INSERT INTO address (road, neighborhood, city, uf, postcode) VALUES
('Rua das Flores, 123', 'Centro', 'São Paulo', 'SP', '01010-100'),
('Avenida Brasil, 456', 'Zona Sul', 'Rio de Janeiro', 'RJ', '22040-300'),
('Rua XV de Novembro, 789', 'Centro', 'Belo Horizonte', 'MG', '30130-120'),
('Rua das Acácias, 234', 'Jardim das Flores', 'Curitiba', 'PR', '80010-080'),
('Avenida Paulista, 555', 'Bela Vista', 'São Paulo', 'SP', '01310-000'),
('Rua do Sol, 890', 'Zona Norte', 'Brasília', 'DF', '70710-010'),
('Rua das Pedras, 567', 'Copacabana', 'Rio de Janeiro', 'RJ', '22050-100'),
('Rua São João, 123', 'Centro', 'Fortaleza', 'CE', '60010-020'),
('Avenida Atlântica, 321', 'Leme', 'Rio de Janeiro', 'RJ', '22010-002'),
('Rua das Palmeiras, 456', 'Vila Mariana', 'São Paulo', 'SP', '04114-020');
