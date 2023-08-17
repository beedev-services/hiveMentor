-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: localhost    Database: thehives_hivementor
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `coreApp_live`
--

DROP TABLE IF EXISTS `coreApp_live`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreApp_live` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dateOfRelease` date NOT NULL,
  `live` tinyint(1) NOT NULL,
  `liveFeature_id` bigint NOT NULL,
  `liveVersion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `coreApp_live_liveFeature_id_5e9e2a7b_fk_coreApp_feature_id` (`liveFeature_id`),
  KEY `coreApp_live_liveVersion_id_1afad099_fk_coreApp_version_id` (`liveVersion_id`),
  CONSTRAINT `coreApp_live_liveFeature_id_5e9e2a7b_fk_coreApp_feature_id` FOREIGN KEY (`liveFeature_id`) REFERENCES `coreApp_feature` (`id`),
  CONSTRAINT `coreApp_live_liveVersion_id_1afad099_fk_coreApp_version_id` FOREIGN KEY (`liveVersion_id`) REFERENCES `coreApp_version` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreApp_live`
--

LOCK TABLES `coreApp_live` WRITE;
/*!40000 ALTER TABLE `coreApp_live` DISABLE KEYS */;
INSERT INTO `coreApp_live` VALUES (1,'2023-08-07',1,1,1),(2,'2023-08-07',1,2,1),(3,'2023-08-07',1,3,1),(4,'2023-08-07',1,4,1);
/*!40000 ALTER TABLE `coreApp_live` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-07 22:58:57
