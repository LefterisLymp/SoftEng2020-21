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
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(64) DEFAULT NULL,
  `type_` varchar(64) DEFAULT NULL,
  `charger_type` varchar(64) DEFAULT NULL,
  `usable_battery_size` int DEFAULT NULL,
  `average_consumption` int DEFAULT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES (1,'kia','crossover','5-pins',36,26,10),(2,'subaru','pickup','7-pins',25,18,11),(3,'toyota','van','7-pins',33,19,12),(4,'vw','hatchback','7-pins',39,16,13),(5,'bmw','hatchback','CCS',35,21,14),(6,'bmw','hatchback','CHAdeMO',29,18,15),(7,'audi','crossover','CHAdeMO',26,20,16),(8,'vw','compact','7-pins',29,16,17),(9,'vw','pickup','CHAdeMO',30,23,18),(10,'audi','crossover','CHAdeMO',34,23,19),(11,'volvo','van','5-pins',35,29,20),(12,'tesla','van','5-pins',35,30,21),(13,'vw','sport','CHAdeMO',33,17,22),(14,'kia','pickup','5-pins',25,22,23),(15,'kia','sport','5-pins',36,19,24),(16,'bmw','pickup','CCS',39,23,25),(17,'toyota','hatchback','CCS',33,22,26),(18,'audi','compact','CCS',27,20,27),(19,'subaru','van','5-pins',27,28,28),(20,'vw','hatchback','CHAdeMO',40,22,29),(21,'volvo','sport','7-pins',40,25,30),(22,'jeep','sport','CHAdeMO',30,22,31),(23,'nissan','pickup','7-pins',31,21,32),(24,'vw','crossover','CCS',27,15,33),(25,'kia','van','CHAdeMO',32,27,34),(26,'toyota','compact','7-pins',37,29,35),(27,'audi','compact','CHAdeMO',25,25,36),(28,'fiat','crossover','7-pins',39,27,37),(29,'nissan','pickup','5-pins',28,22,38),(30,'subaru','compact','5-pins',38,27,39),(31,'volvo','van','5-pins',34,28,40),(32,'jeep','hatchback','5-pins',27,21,41),(33,'toyota','pickup','CHAdeMO',34,19,42),(34,'kia','compact','CHAdeMO',27,24,43),(35,'vw','van','CHAdeMO',30,20,44),(36,'jeep','compact','CCS',26,21,45),(37,'tesla','compact','CHAdeMO',25,28,46),(38,'suzuki','pickup','7-pins',35,18,47),(39,'vw','crossover','5-pins',28,23,48),(40,'suzuki','sport','7-pins',35,25,49);
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-11 13:53:52
