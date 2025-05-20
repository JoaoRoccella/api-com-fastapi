CREATE DATABASE IF NOT EXISTS `mustwatch` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE `mustwatch`;

CREATE TABLE IF NOT EXISTS `serie` (
    `id_serie` INT(11) NOT NULL AUTO_INCREMENT,
    `titulo` VARCHAR(100) NOT NULL,
    `descricao` TEXT NOT NULL,
    `ano_lancamento` YEAR(4) NOT NULL,
    `id_categoria` TINYINT(3) NOT NULL,
    PRIMARY KEY (`id_serie`),
    CONSTRAINT `fk_categoria_serie` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`)
);

CREATE TABLE IF NOT EXISTS `categoria` (
    `id_categoria` TINYINT(3) NOT NULL AUTO_INCREMENT,
    `nome` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id_categoria`)
);

CREATE TABLE IF NOT EXISTS `ator` (
    `id_ator` INT(11) NOT NULL AUTO_INCREMENT,
    `nome` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`id_ator`)
);

CREATE TABLE IF NOT EXISTS `ator_serie` (
    `id_ator` INT(11) NOT NULL,
    `id_serie` INT(11) NOT NULL,
    `personagem` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`id_ator`, `id_serie`),
    CONSTRAINT `fk_ator_serie` FOREIGN KEY (`id_ator`) REFERENCES `ator` (`id_ator`),
    CONSTRAINT `fk_serie_ator` FOREIGN KEY (`id_serie`) REFERENCES `serie` (`id_serie`)
);

CREATE TABLE IF NOT EXISTS `motivo_assistir` (
    `id_motivo` INT(11) NOT NULL AUTO_INCREMENT,
    `id_serie` INT(11) NOT NULL,
    `motivo` TEXT NOT NULL,
    PRIMARY KEY (`id_motivo`),
    CONSTRAINT `fk_serie_motivo` FOREIGN KEY (`id_serie`) REFERENCES `serie` (`id_serie`)
);

CREATE TABLE IF NOT EXISTS `avaliacao_serie` (
    `id_avaliacao` INT(11) NOT NULL AUTO_INCREMENT,
    `id_serie` INT(11) NOT NULL,
    `nota` TINYINT(2) NOT NULL,
    `comentario` TEXT NOT NULL,
    `data_avaliacao` DATETIME NOT NULL,
    PRIMARY KEY (`id_avaliacao`),
    CONSTRAINT `fk_serie_avaliacao` FOREIGN KEY (`id_serie`) REFERENCES `serie` (`id_serie`),
    CONSTRAINT `chk_nota` CHECK (`nota` BETWEEN 1 AND 10)
);
    