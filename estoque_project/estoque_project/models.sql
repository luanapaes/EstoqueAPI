-- Tabela Empresa

CREATE TABLE empresa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    cnpj VARCHAR(14) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
);

-- Tabela Funcionário

CREATE TABLE funcionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    cargo VARCHAR(255) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    empresa_id INTEGER,
    FOREIGN KEY (empresa_id) REFERENCES empresa(id)
);

-- Tabela Produto

CREATE TABLE produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    empresa_id INTEGER,
    FOREIGN KEY (empresa_id) REFERENCES empresa(id)
);
