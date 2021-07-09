CREATE DATABASE  IF NOT EXISTS `progettobdd` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `progettobdd`;
-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: progettobdd
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `articolo`
--

DROP TABLE IF EXISTS `articolo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `articolo` (
  `IdArticolo` int NOT NULL AUTO_INCREMENT,
  `Articolo` varchar(45) NOT NULL,
  `NomePubblicatore` varchar(45) NOT NULL,
  `Data` date DEFAULT NULL,
  `Link` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`IdArticolo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articolo`
--

LOCK TABLES `articolo` WRITE;
/*!40000 ALTER TABLE `articolo` DISABLE KEYS */;
INSERT INTO `articolo` VALUES (1,'---','---','0000-00-00','---'),(2,'David(Michelangelo)','Wikipedia','0000-00-00','https://it.wikipedia.org/wiki/David_(Michelangelo)'),(3,'EsempioArticoloMultirelatore','MultiRelatore','0000-00-00','---');
/*!40000 ALTER TABLE `articolo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `autore`
--

DROP TABLE IF EXISTS `autore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autore` (
  `IdAutore` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  PRIMARY KEY (`IdAutore`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autore`
--

LOCK TABLES `autore` WRITE;
/*!40000 ALTER TABLE `autore` DISABLE KEYS */;
INSERT INTO `autore` VALUES (1,'---'),(2,'Michelangelo Buonarroti'),(3,'Neil Gaiman'),(4,'Leonardo Da Vinci'),(5,'Nintendo'),(6,'Kanagawa'),(7,'Marvel'),(8,'Metallica');
/*!40000 ALTER TABLE `autore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campione`
--

DROP TABLE IF EXISTS `campione`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campione` (
  `idCampione` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `DataP` date DEFAULT NULL,
  `DataC` date DEFAULT NULL,
  `LuogoC` varchar(45) DEFAULT NULL,
  `Descrizione` varchar(8000) DEFAULT NULL,
  `IdStato` smallint NOT NULL,
  `IdOpera` int NOT NULL,
  `IdLaboratorio` int DEFAULT NULL,
  PRIMARY KEY (`idCampione`),
  KEY `IdStato_idx` (`IdStato`),
  KEY `IdOpera_idx` (`IdOpera`),
  KEY `IdLaboratorio_idx` (`IdLaboratorio`),
  CONSTRAINT `IdLaboratorio` FOREIGN KEY (`IdLaboratorio`) REFERENCES `laboratorio` (`IdLaboratorio`),
  CONSTRAINT `IdOpera` FOREIGN KEY (`IdOpera`) REFERENCES `opera` (`IdOpera`),
  CONSTRAINT `IdStato` FOREIGN KEY (`IdStato`) REFERENCES `stato` (`idStato`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campione`
--

LOCK TABLES `campione` WRITE;
/*!40000 ALTER TABLE `campione` DISABLE KEYS */;
INSERT INTO `campione` VALUES (1,'da001','2020-09-08','2021-07-08','Mobile1','Lorem Ipsum ',1,2,1),(2,'da002','1994-05-13','2021-07-08','Museo3','Il David è una scultura realizzata in marmo (altezza 520 cm incluso il basamento di 108 cm) da Michelangelo Buonarroti, databile tra il 1501 e l\'inizio del 1504 e conservata nella Galleria dell\'Accademia a Firenze.',2,2,3),(3,'da003','0000-00-00','2021-07-08','Smarrito','Smarrito',1,2,1),(4,'ca001','2020-02-02','2021-07-08','Cassetto13','Il 16 agosto del 1501 i consoli dell\'Arte della Lana e l’Opera del Duomo di Firenze commissionarono a Michelangelo una statua di re David.',2,3,1),(5,'ca002','0000-00-00','2021-07-08','Libreria2','---',1,3,1),(6,'mu001','1990-09-09','1998-08-08','Scrivania3','Un esempio di come un articolo può essere linkato a più relatori, per poterlo stampare per intero.',1,4,1),(7,'gi001','2013-04-05','2021-07-08','Laboratorio8','La Gioconda, nota anche come Monna Lisa, è un dipinto a olio su tavola di legno di pioppo realizzato da Leonardo da Vinci, ',2,5,1),(8,'gi002','0000-00-00','2021-07-08','---','---',1,5,1),(9,'fungo','2021-07-07','2021-07-08','Casa di Ilaria','è un fungo rosso con i pallini bianchi ed è molto amico di super mario',1,6,1),(10,'Franco','2021-07-07','2021-07-08','Tsuki','Franco è un topo blu con le orecchie grandi e il suo piatto preferito è pasta e ceci',1,8,1),(11,'Ilaria','1995-10-04','2021-07-08','Collegi','Mi piace il rosa, il rosso, animal crossing e i chicken nugget',2,4,1),(12,'go001','0000-00-00','2021-07-08','Cassetto9','Di dimensioni 25,7 × 37,9 cm, raffigura un\'onda tempestosa che minaccia alcune imbarcazioni al largo di una zona corrispondente all\'odierna prefettura di Kanagawa; come in tutte le altre rappresentazioni di questa serie sullo sfondo compare il Monte Fuji. Sebbene venga vista come l\'opera che più rappresenta l\'arte giapponese,',1,9,1),(13,'ds001','0000-00-00','2021-07-08','sala cinematografica','doctor strange è un film sui supereroi interpretato da benedict cumberbatch',1,10,1),(14,'bl001','0000-00-00','2021-07-08','Spotify','un pezzo della canzone	',1,11,1),(16,'test','0000-00-00','2021-07-08','---','test',1,11,1),(17,'test1','0000-00-00','2021-07-08','---','---',1,12,1);
/*!40000 ALTER TABLE `campione` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citato`
--

DROP TABLE IF EXISTS `citato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citato` (
  `IdCampione` int NOT NULL,
  `IdArticolo` int NOT NULL,
  KEY `IdArticolo_idx` (`IdArticolo`),
  KEY `IdCampione_idx` (`IdCampione`),
  CONSTRAINT `IdArticolo` FOREIGN KEY (`IdArticolo`) REFERENCES `articolo` (`IdArticolo`) ON DELETE CASCADE,
  CONSTRAINT `IdCampione` FOREIGN KEY (`IdCampione`) REFERENCES `campione` (`idCampione`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citato`
--

LOCK TABLES `citato` WRITE;
/*!40000 ALTER TABLE `citato` DISABLE KEYS */;
INSERT INTO `citato` VALUES (1,1),(2,2),(3,1),(4,1),(5,1),(6,3),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),(13,1),(14,1),(16,1),(17,1);
/*!40000 ALTER TABLE `citato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laboratorio`
--

DROP TABLE IF EXISTS `laboratorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laboratorio` (
  `IdLaboratorio` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `DataInvio` date DEFAULT NULL,
  PRIMARY KEY (`IdLaboratorio`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laboratorio`
--

LOCK TABLES `laboratorio` WRITE;
/*!40000 ALTER TABLE `laboratorio` DISABLE KEYS */;
INSERT INTO `laboratorio` VALUES (1,'---','0000-00-00'),(2,'---','0000-00-00'),(3,'Lab2','2021-03-03'),(4,'---','0000-00-00'),(5,'---','0000-00-00'),(6,'---','0000-00-00'),(7,'---','0000-00-00'),(8,'---','0000-00-00'),(9,'---','0000-00-00'),(10,'---','0000-00-00'),(12,'---','0000-00-00'),(13,'---','0000-00-00'),(14,'---','0000-00-00'),(15,'---','0000-00-00'),(16,'---','0000-00-00'),(17,'---','0000-00-00'),(18,'---','0000-00-00'),(19,'---','0000-00-00');
/*!40000 ALTER TABLE `laboratorio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `opera`
--

DROP TABLE IF EXISTS `opera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `opera` (
  `IdOpera` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Periodo` varchar(45) DEFAULT NULL,
  `Tipologia` varchar(45) DEFAULT NULL,
  `IdAutore` int DEFAULT NULL,
  `IdProvenienza` int NOT NULL,
  PRIMARY KEY (`IdOpera`),
  KEY `IdAutore_idx` (`IdAutore`),
  KEY `IdProvenienza_idx` (`IdProvenienza`),
  CONSTRAINT `IdAutore` FOREIGN KEY (`IdAutore`) REFERENCES `autore` (`IdAutore`),
  CONSTRAINT `IdProvenienza` FOREIGN KEY (`IdProvenienza`) REFERENCES `provenienza` (`IdProvenienza`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `opera`
--

LOCK TABLES `opera` WRITE;
/*!40000 ALTER TABLE `opera` DISABLE KEYS */;
INSERT INTO `opera` VALUES (1,'---','---','---',NULL,1),(2,'Il David','1500','Statua',2,2),(3,'Buona Apocalisse a Tutti','2016','Libro',3,3),(4,'---','---','---',1,1),(5,'La Gioconda','1506','Quadro',4,4),(6,'Super Mario','1980','Videogioco',5,5),(8,'Animal Crossing','2018','Videogioco',5,5),(9,'La grande onda','1830','Quadro',6,6),(10,'Doctor Strange','2016','Film',7,1),(11,'Master of Puppets','1986','Musica',8,1),(12,'Master of Puppets','1986','Musica',8,8);
/*!40000 ALTER TABLE `opera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provenienza`
--

DROP TABLE IF EXISTS `provenienza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provenienza` (
  `IdProvenienza` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Comune` varchar(45) NOT NULL,
  `Provincia` varchar(45) NOT NULL,
  PRIMARY KEY (`IdProvenienza`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provenienza`
--

LOCK TABLES `provenienza` WRITE;
/*!40000 ALTER TABLE `provenienza` DISABLE KEYS */;
INSERT INTO `provenienza` VALUES (1,'---','---','---'),(2,'Galleria dell\'Accademia','Firenze','FI'),(3,'Libreria Cagli','Cagli','PU'),(4,'Louvres','Francia','---'),(5,'Nintendo','Giappone','---'),(6,'Biblioteca del Congresso','Stati Uniti','---'),(7,'Elektra Records','Stati Uniti','---'),(8,'USA','USA','USA');
/*!40000 ALTER TABLE `provenienza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `relatore`
--

DROP TABLE IF EXISTS `relatore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `relatore` (
  `IdRelatore` int NOT NULL,
  `Nome` varchar(45) NOT NULL,
  `Afferenza` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`IdRelatore`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `relatore`
--

LOCK TABLES `relatore` WRITE;
/*!40000 ALTER TABLE `relatore` DISABLE KEYS */;
INSERT INTO `relatore` VALUES (1,'---','---'),(2,'Jhon Doe','---'),(3,'Jane Doe','Università del Massachusetts');
/*!40000 ALTER TABLE `relatore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scritto`
--

DROP TABLE IF EXISTS `scritto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scritto` (
  `IdArticolo` int NOT NULL,
  `IdRelatore` int NOT NULL,
  KEY `IdArticolo_idx` (`IdArticolo`),
  KEY `IdRelatore_idx` (`IdRelatore`),
  CONSTRAINT `IdArticolo1` FOREIGN KEY (`IdArticolo`) REFERENCES `articolo` (`IdArticolo`) ON DELETE CASCADE,
  CONSTRAINT `IdRelatore` FOREIGN KEY (`IdRelatore`) REFERENCES `relatore` (`IdRelatore`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scritto`
--

LOCK TABLES `scritto` WRITE;
/*!40000 ALTER TABLE `scritto` DISABLE KEYS */;
INSERT INTO `scritto` VALUES (1,1),(2,1),(3,2),(3,3);
/*!40000 ALTER TABLE `scritto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stato`
--

DROP TABLE IF EXISTS `stato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stato` (
  `idStato` smallint NOT NULL,
  `Nome` varchar(45) NOT NULL,
  PRIMARY KEY (`idStato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stato`
--

LOCK TABLES `stato` WRITE;
/*!40000 ALTER TABLE `stato` DISABLE KEYS */;
INSERT INTO `stato` VALUES (1,'Tal Quale'),(2,'Sezione Lucida');
/*!40000 ALTER TABLE `stato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'progettobdd'
--

--
-- Dumping routines for database 'progettobdd'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-08 18:55:46
