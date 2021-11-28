-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema schema_movies
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema schema_movies
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `schema_movies` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `schema_movies` ;

-- -----------------------------------------------------
-- Table `schema_movies`.`Movie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_movies`.`Movie` (
  `IDMovie` INT NOT NULL AUTO_INCREMENT,
  `movie_name` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`IDMovie`))
ENGINE = InnoDB
AUTO_INCREMENT = 89
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `schema_movies`.`Context`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_movies`.`Context` (
  `IDContext` INT NOT NULL AUTO_INCREMENT,
  `context_name` VARCHAR(200) NULL DEFAULT NULL,
  `Movie_IDMovie` INT NOT NULL,
  PRIMARY KEY (`IDContext`),
  INDEX `fk_Context_Movie1_idx` (`Movie_IDMovie` ASC) VISIBLE,
  CONSTRAINT `fk_Context_Movie1`
    FOREIGN KEY (`Movie_IDMovie`)
    REFERENCES `schema_movies`.`Movie` (`IDMovie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `schema_movies`.`Phrases`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `schema_movies`.`Phrases` (
  `IDPhrases` INT NOT NULL AUTO_INCREMENT,
  `phrases_name` VARCHAR(1000) NULL DEFAULT NULL,
  `Context_IDContext` INT NOT NULL,
  `Movie_IDMovie` INT NOT NULL,
  PRIMARY KEY (`IDPhrases`),
  INDEX `fk_Phrases_Context_idx` (`Context_IDContext` ASC) VISIBLE,
  INDEX `fk_Phrases_Movie1_idx` (`Movie_IDMovie` ASC) VISIBLE,
  CONSTRAINT `fk_Phrases_Context`
    FOREIGN KEY (`Context_IDContext`)
    REFERENCES `schema_movies`.`Context` (`IDContext`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Phrases_Movie1`
    FOREIGN KEY (`Movie_IDMovie`)
    REFERENCES `schema_movies`.`Movie` (`IDMovie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
