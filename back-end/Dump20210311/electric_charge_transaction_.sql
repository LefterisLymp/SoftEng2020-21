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
-- Table structure for table `transaction_`
--

DROP TABLE IF EXISTS `transaction_`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_` (
  `id` int NOT NULL AUTO_INCREMENT,
  `charge_id` int NOT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  `points` int DEFAULT NULL,
  `payment_method` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_`
--

LOCK TABLES `transaction_` WRITE;
/*!40000 ALTER TABLE `transaction_` DISABLE KEYS */;
INSERT INTO `transaction_` VALUES (1000,1,3.00,25,'cash'),(1001,2,1.00,14,'credit'),(1002,3,6.00,32,'credit'),(1003,4,7.00,62,'credit'),(1004,5,10.00,97,'debit'),(1005,6,9.00,69,'debit'),(1006,7,9.00,67,'debit'),(1007,8,10.00,79,'debit'),(1008,9,4.00,29,'credit'),(1009,10,10.00,37,'credit'),(1010,11,9.00,90,'debit'),(1011,12,6.00,80,'debit'),(1012,13,8.00,80,'credit'),(1013,14,2.00,67,'cash'),(1014,15,6.00,24,'credit'),(1015,16,9.00,55,'credit'),(1016,17,6.00,80,'debit'),(1017,18,9.00,70,'cash'),(1018,19,10.00,82,'cash'),(1019,20,5.00,17,'credit'),(1020,21,2.00,77,'cash'),(1021,22,2.00,81,'cash'),(1022,23,8.00,56,'debit'),(1023,24,8.00,19,'debit'),(1024,25,3.00,62,'credit'),(1025,26,6.00,19,'cash'),(1026,27,4.00,75,'cash'),(1027,28,9.00,65,'debit'),(1028,29,2.00,73,'cash'),(1029,30,4.00,55,'debit'),(1030,31,1.00,59,'debit'),(1031,32,6.00,14,'debit'),(1032,33,4.00,80,'credit'),(1033,34,10.00,98,'cash'),(1034,35,6.00,100,'credit'),(1035,36,9.00,70,'credit'),(1036,37,6.00,56,'debit'),(1037,38,1.00,15,'debit'),(1038,39,7.00,67,'debit'),(1039,40,5.00,56,'debit'),(1040,41,8.00,12,'credit'),(1041,42,5.00,40,'cash'),(1042,43,1.00,69,'cash'),(1043,44,10.00,78,'cash'),(1044,45,6.00,60,'debit'),(1045,46,4.00,35,'cash'),(1046,47,7.00,65,'debit'),(1047,48,8.00,79,'credit'),(1048,49,4.00,15,'debit'),(1049,50,3.00,20,'cash'),(1050,51,1.00,97,'debit'),(1051,52,3.00,64,'debit'),(1052,53,8.00,70,'cash'),(1053,54,1.00,80,'cash'),(1054,55,7.00,99,'cash'),(1055,56,10.00,33,'cash'),(1056,57,1.00,52,'cash'),(1057,58,3.00,33,'credit'),(1058,59,5.00,97,'cash'),(1059,60,4.00,28,'debit'),(1060,61,1.00,82,'debit'),(1061,62,2.00,89,'debit'),(1062,63,7.00,80,'cash'),(1063,64,10.00,36,'debit'),(1064,65,5.00,86,'debit'),(1065,66,10.00,73,'debit'),(1066,67,2.00,41,'debit'),(1067,68,6.00,42,'debit'),(1068,69,8.00,61,'credit'),(1069,70,5.00,60,'debit'),(1070,71,4.00,14,'debit'),(1071,72,1.00,71,'cash'),(1072,73,8.00,12,'cash'),(1073,74,4.00,93,'cash'),(1074,75,3.00,99,'cash'),(1075,76,7.00,91,'credit'),(1076,77,8.00,82,'cash'),(1077,78,6.00,65,'cash'),(1078,79,6.00,44,'debit'),(1079,80,3.00,52,'credit'),(1080,81,8.00,60,'debit'),(1081,82,1.00,27,'debit'),(1082,83,2.00,80,'cash'),(1083,84,5.00,97,'cash'),(1084,85,3.00,33,'debit'),(1085,86,6.00,100,'cash'),(1086,87,3.00,72,'cash'),(1087,88,9.00,19,'credit'),(1088,89,10.00,42,'credit'),(1089,90,9.00,98,'debit'),(1090,91,10.00,48,'cash'),(1091,92,10.00,81,'debit'),(1092,93,9.00,33,'cash'),(1093,94,10.00,54,'debit'),(1094,95,3.00,98,'credit'),(1095,96,7.00,98,'cash'),(1096,97,4.00,27,'debit'),(1097,98,2.00,40,'debit'),(1098,99,5.00,75,'cash'),(1099,100,4.00,37,'debit'),(1100,101,5.00,80,'credit'),(1101,102,2.00,51,'credit'),(1103,103,8.00,10,'debit'),(1104,104,5.00,58,'cash'),(1105,105,1.00,59,'debit'),(1106,106,8.00,81,'cash'),(1107,107,10.00,67,'credit'),(1108,108,9.00,76,'debit'),(1109,109,9.00,13,'debit'),(1110,110,10.00,68,'cash'),(1111,111,6.00,69,'credit'),(1112,112,4.00,32,'credit');
/*!40000 ALTER TABLE `transaction_` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-11 13:53:34
