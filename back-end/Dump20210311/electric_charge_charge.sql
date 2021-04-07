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
-- Table structure for table `charge`
--

DROP TABLE IF EXISTS `charge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `charge` (
  `id` int NOT NULL AUTO_INCREMENT,
  `chargingpoint_id` varchar(64) DEFAULT NULL,
  `vehicle_id` int DEFAULT NULL,
  `kWhdelivered` int DEFAULT NULL,
  `connection_time` timestamp NULL DEFAULT NULL,
  `disconnection_time` timestamp NULL DEFAULT NULL,
  `date_` date DEFAULT NULL,
  `provider_id` int DEFAULT NULL,
  `price_policy_ref` varchar(64) DEFAULT NULL,
  `cost_per_kwh` decimal(5,2) DEFAULT NULL,
  `protocol` varchar(64) DEFAULT NULL,
  `total_cost` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `charge`
--

LOCK TABLES `charge` WRITE;
/*!40000 ALTER TABLE `charge` DISABLE KEYS */;
INSERT INTO `charge` VALUES (1,'5809 In St._1',29,27,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',7,'credit',2.00,'low',4.00),(2,'725-3717 Orci Rd._3',20,23,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',19,'credit',1.00,'high',4.00),(3,'3731 Auctor, Street_1',38,24,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',10,'cash',1.00,'high',4.00),(4,'7983 Gravida Av._4',35,9,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',12,'paypal',1.00,'low',3.00),(5,'228-8595 Integer Street_4',6,7,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',21,'cash',1.00,'medium',4.00),(6,'8997 Mauris. Road_2',7,5,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',3,'debit',2.00,'high',3.00),(7,'725-3717 Orci Rd._1',26,10,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',8,'credit',2.00,'medium',3.00),(8,'P.O. Box 304, 3274 Dictum St._0',27,5,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',16,'credit',2.00,'low',3.00),(9,'5809 In St._2',14,35,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',12,'cash',1.00,'low',3.00),(10,'188-2300 Lacus Rd._1',12,40,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',18,'credit',2.00,'medium',3.00),(11,'P.O. Box 111, 8901 Mauris Road_0',5,27,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',11,'debit',2.00,'medium',3.00),(12,'P.O. Box 411, 7458 Malesuada St._4',13,2,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',9,'debit',1.00,'medium',3.00),(13,'P.O. Box 485, 512 Et Rd._4',13,4,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',18,'credit',2.00,'medium',3.00),(14,'725-3717 Orci Rd._4',28,36,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',18,'credit',1.00,'medium',3.00),(15,'Ap #665-6394 Donec Avenue_3',32,29,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',14,'paypal',2.00,'high',3.00),(16,'5809 In St._1',5,6,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',19,'debit',1.00,'high',3.00),(17,'Ap #743-9316 Pellentesque Rd._3',8,5,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',9,'paypal',2.00,'high',4.00),(18,'5809 In St._4',15,32,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',20,'credit',2.00,'high',4.00),(19,'P.O. Box 111, 8901 Mauris Road_4',11,37,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',10,'debit',1.00,'medium',4.00),(20,'Ap #812-5236 Eu Road_2',4,26,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',5,'cash',2.00,'medium',3.00),(21,'P.O. Box 657, 6471 Tristique Avenue_2',8,15,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',9,'debit',1.00,'high',3.00),(22,'262-1582 At Rd._1',35,32,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',1,'debit',1.00,'low',3.00),(23,'P.O. Box 304, 3274 Dictum St._0',11,9,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',19,'credit',1.00,'medium',4.00),(24,'3731 Auctor, Street_4',31,10,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',14,'credit',2.00,'medium',3.00),(25,'Ap #743-9316 Pellentesque Rd._4',39,24,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',21,'credit',1.00,'medium',3.00),(26,'Ap #284-3574 Scelerisque Rd._2',7,29,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',5,'credit',2.00,'low',4.00),(27,'195-6694 Sit Rd._2',32,22,'2020-04-13 08:42:41','2020-04-13 10:42:41','2020-04-13',7,'paypal',2.00,'high',3.00),(28,'P.O. Box 901, 7334 Pellentesque Road_1',18,12,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',15,'paypal',1.00,'medium',3.00),(29,'8997 Mauris. Road_0',25,33,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',19,'paypal',1.00,'high',4.00),(30,'Ap #284-3574 Scelerisque Rd._1',32,40,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',11,'paypal',2.00,'medium',4.00),(31,'8997 Mauris. Road_2',6,34,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',10,'paypal',2.00,'low',4.00),(32,'Ap #812-5236 Eu Road_1',22,18,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',17,'credit',1.00,'high',3.00),(33,'Ap #431-681 Gravida Street_2',8,12,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',8,'cash',2.00,'medium',4.00),(34,'Ap #465-462 Donec Av._4',23,28,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',2,'credit',1.00,'high',4.00),(35,'725-3717 Orci Rd._3',18,25,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',2,'cash',2.00,'high',4.00),(36,'8997 Mauris. Road_3',27,17,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',13,'paypal',1.00,'high',3.00),(37,'Ap #743-9316 Pellentesque Rd._1',12,9,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',7,'cash',1.00,'high',3.00),(38,'242-7155 Nullam Av._3',9,8,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',8,'paypal',2.00,'high',3.00),(39,'P.O. Box 901, 7334 Pellentesque Road_1',5,14,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',10,'credit',2.00,'medium',4.00),(40,'228-8595 Integer Street_2',3,34,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',12,'cash',1.00,'high',4.00),(41,'228-8595 Integer Street_2',10,5,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',9,'cash',2.00,'high',4.00),(42,'Ap #284-3574 Scelerisque Rd._0',18,34,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',18,'debit',1.00,'low',3.00),(43,'Ap #392-6995 Sit St._3',19,20,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',3,'debit',2.00,'high',4.00),(44,'1978 Rutrum Road_1',14,16,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',1,'debit',2.00,'high',4.00),(45,'242-7155 Nullam Av._0',22,32,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',11,'paypal',2.00,'medium',4.00),(46,'Ap #812-5236 Eu Road_3',34,30,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',14,'debit',2.00,'high',4.00),(47,'P.O. Box 411, 7458 Malesuada St._1',25,14,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',8,'cash',2.00,'high',3.00),(48,'571-5772 In, Street_4',17,18,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',11,'credit',2.00,'low',3.00),(49,'Ap #431-681 Gravida Street_1',25,4,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',7,'debit',1.00,'high',4.00),(50,'8791 Ut St._2',29,28,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',17,'cash',2.00,'medium',4.00),(51,'188-2300 Lacus Rd._3',17,18,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',13,'cash',1.00,'medium',3.00),(52,'Ap #665-6394 Donec Avenue_0',9,37,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',7,'credit',2.00,'high',4.00),(53,'1131 Nec Av._0',29,4,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',20,'credit',1.00,'medium',3.00),(54,'P.O. Box 657, 6471 Tristique Avenue_1',23,12,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',2,'debit',1.00,'low',3.00),(55,'262-1582 At Rd._1',7,35,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',5,'paypal',2.00,'low',3.00),(56,'P.O. Box 249, 6427 Velit Rd._1',37,22,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',16,'debit',2.00,'low',3.00),(57,'P.O. Box 111, 8901 Mauris Road_3',24,13,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',21,'credit',2.00,'medium',4.00),(58,'Ap #431-681 Gravida Street_0',12,37,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',4,'debit',1.00,'low',4.00),(59,'Ap #812-5236 Eu Road_1',29,14,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',11,'cash',2.00,'medium',3.00),(60,'P.O. Box 485, 512 Et Rd._0',28,39,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',16,'cash',1.00,'medium',3.00),(61,'1131 Nec Av._2',35,31,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',12,'credit',2.00,'medium',4.00),(62,'Ap #665-6394 Donec Avenue_3',7,6,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',11,'credit',1.00,'high',4.00),(63,'228-8595 Integer Street_4',1,37,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',6,'cash',1.00,'high',3.00),(64,'P.O. Box 265, 9646 Nostra, Rd._3',21,28,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',10,'credit',2.00,'high',3.00),(65,'P.O. Box 901, 7334 Pellentesque Road_1',8,40,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',19,'credit',1.00,'high',4.00),(66,'1131 Nec Av._3',7,25,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',4,'debit',1.00,'medium',4.00),(67,'Ap #465-462 Donec Av._2',34,3,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',1,'credit',2.00,'high',4.00),(68,'8791 Ut St._1',20,11,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',3,'debit',2.00,'low',4.00),(69,'P.O. Box 901, 7334 Pellentesque Road_4',37,35,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',8,'credit',1.00,'low',3.00),(70,'P.O. Box 249, 6427 Velit Rd._4',32,26,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',13,'cash',1.00,'medium',3.00),(71,'242-7155 Nullam Av._1',13,29,'2020-04-16 08:45:41','2020-04-16 14:45:41','2020-04-16',14,'paypal',2.00,'low',4.00),(72,'P.O. Box 901, 7334 Pellentesque Road_4',37,37,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',14,'cash',1.00,'medium',4.00),(73,'5809 In St._1',39,6,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',4,'credit',1.00,'high',3.00),(74,'Ap #743-9316 Pellentesque Rd._3',36,36,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',12,'cash',1.00,'low',4.00),(75,'188-2300 Lacus Rd._4',35,14,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',14,'credit',1.00,'medium',4.00),(76,'Ap #431-681 Gravida Street_3',16,7,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',4,'cash',2.00,'medium',4.00),(77,'P.O. Box 249, 6427 Velit Rd._3',5,16,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',4,'debit',1.00,'medium',4.00),(78,'8997 Mauris. Road_1',12,8,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',6,'credit',2.00,'medium',3.00),(79,'3731 Auctor, Street_2',12,30,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',16,'cash',1.00,'high',3.00),(80,'P.O. Box 249, 6427 Velit Rd._4',9,29,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',10,'paypal',1.00,'low',3.00),(81,'P.O. Box 265, 9646 Nostra, Rd._0',20,16,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',20,'debit',1.00,'high',4.00),(82,'228-8595 Integer Street_3',1,16,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',15,'paypal',2.00,'high',4.00),(83,'P.O. Box 111, 8901 Mauris Road_0',4,6,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',16,'paypal',1.00,'low',4.00),(84,'P.O. Box 249, 6427 Velit Rd._2',31,8,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',4,'paypal',1.00,'low',4.00),(85,'P.O. Box 304, 3274 Dictum St._1',23,7,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',9,'debit',2.00,'high',4.00),(86,'5809 In St._3',15,18,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',1,'debit',2.00,'medium',4.00),(87,'P.O. Box 249, 6427 Velit Rd._3',17,14,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',7,'debit',1.00,'high',4.00),(88,'5809 In St._1',35,10,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',12,'paypal',2.00,'low',3.00),(89,'P.O. Box 901, 7334 Pellentesque Road_2',1,3,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',15,'paypal',1.00,'low',3.00),(90,'188-2300 Lacus Rd._4',16,36,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',5,'credit',1.00,'medium',3.00),(91,'3731 Auctor, Street_0',3,38,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',1,'cash',1.00,'medium',3.00),(92,'P.O. Box 411, 7458 Malesuada St._4',20,37,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',18,'cash',1.00,'low',3.00),(93,'P.O. Box 265, 9646 Nostra, Rd._2',7,6,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',8,'paypal',1.00,'medium',4.00),(94,'P.O. Box 249, 6427 Velit Rd._4',2,15,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',2,'debit',1.00,'high',3.00),(95,'725-3717 Orci Rd._4',15,20,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',1,'cash',1.00,'low',3.00),(96,'1978 Rutrum Road_1',33,15,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',16,'debit',2.00,'medium',4.00),(97,'8791 Ut St._4',34,22,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',3,'cash',2.00,'medium',3.00),(98,'8791 Ut St._1',21,26,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',15,'cash',2.00,'low',3.00),(99,'P.O. Box 411, 7458 Malesuada St._0',32,4,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',20,'debit',2.00,'low',4.00),(100,'725-3717 Orci Rd._4',27,29,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',14,'credit',2.00,'low',4.00),(101,'Ap #665-6394 Donec Avenue_4',13,13,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',19,'credit',2.00,'medium',4.00),(102,'Ap #431-681 Gravida Street_3',22,30,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',3,'paypal',1.00,'medium',3.00),(103,'5809 In St._4',11,27,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',2,'debit',1.00,'medium',3.00),(104,'Ap #431-681 Gravida Street_4',3,15,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',18,'cash',1.00,'low',3.00),(105,'Ap #391-5939 Odio St._1',2,17,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',21,'credit',1.00,'high',3.00),(106,'Ap #391-5939 Odio St._0',39,9,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',2,'cash',1.00,'medium',3.00),(107,'Ap #465-462 Donec Av._2',2,26,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',16,'paypal',1.00,'medium',3.00),(108,'1131 Nec Av._4',13,27,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',1,'debit',1.00,'high',4.00),(109,'P.O. Box 304, 3274 Dictum St._1',18,38,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',8,'debit',2.00,'medium',4.00),(110,'Ap #391-5939 Odio St._0',8,8,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',8,'debit',1.00,'low',4.00),(111,'P.O. Box 657, 6471 Tristique Avenue_2',7,25,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',18,'credit',1.00,'medium',4.00),(112,'P.O. Box 249, 6427 Velit Rd._0',27,10,'2020-04-18 08:50:41','2020-04-18 12:50:41','2020-04-18',12,'credit',2.00,'high',4.00);
/*!40000 ALTER TABLE `charge` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-11 13:53:45