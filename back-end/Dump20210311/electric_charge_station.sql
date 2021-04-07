-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: electric_charge
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `station`
--

DROP TABLE IF EXISTS `station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `station` (
  `id` varchar(64) NOT NULL,
  `manager_id` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station`
--

LOCK TABLES `station` WRITE;
/*!40000 ALTER TABLE `station` DISABLE KEYS */;
INSERT INTO `station` VALUES ('1131 Nec Av.','Anna Victorino'),('188-2300 Lacus Rd.','Madelaine Hird'),('195-6694 Sit Rd.','Nedra Macmillan'),('1978 Rutrum Road','Leontine Stefano'),('228-8595 Integer Street','Ricky Printup'),('242-7155 Nullam Av.','Wonda Lemmons'),('262-1582 At Rd.','Nickie Hickmon'),('3731 Auctor, Street','Ellie Devillier'),('571-5772 In, Street','Theodore Inouye'),('5809 In St.','Mason Lechler'),('725-3717 Orci Rd.','Marylin Bleich'),('7983 Gravida Av.','Tommy Thoman'),('8791 Ut St.','Hettie Mcclaskey'),('8997 Mauris. Road','Donovan Fragale '),('Ap #284-3574 Scelerisque Rd.','Ellsworth Chumbley'),('Ap #391-5939 Odio St.','Hank Nanney'),('Ap #392-6995 Sit St.','Kory Almquist'),('Ap #431-681 Gravida Street','Cherrie Rohe'),('Ap #465-462 Donec Av.','Claude Poteet'),('Ap #665-6394 Donec Avenue','Marinda Hackler'),('Ap #743-9316 Pellentesque Rd.','Ayako Alejandre'),('Ap #812-5236 Eu Road','Jerome Bushey'),('P.O. Box 111, 8901 Mauris Road','Ngoc Mai'),('P.O. Box 249, 6427 Velit Rd.','Blanca Vicari '),('P.O. Box 265, 9646 Nostra, Rd.','Deandre Eggers'),('P.O. Box 304, 3274 Dictum St.','Lee Quan'),('P.O. Box 411, 7458 Malesuada St.','Starla Bottomley'),('P.O. Box 485, 512 Et Rd.','Abel Karlson '),('P.O. Box 657, 6471 Tristique Avenue','Librada Knabe'),('P.O. Box 901, 7334 Pellentesque Road','Mitsue Crotty');
/*!40000 ALTER TABLE `station` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-11 13:53:47
