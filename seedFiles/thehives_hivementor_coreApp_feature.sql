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
-- Table structure for table `coreApp_feature`
--

DROP TABLE IF EXISTS `coreApp_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coreApp_feature` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `info` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coreApp_feature`
--

LOCK TABLES `coreApp_feature` WRITE;
/*!40000 ALTER TABLE `coreApp_feature` DISABLE KEYS */;
INSERT INTO `coreApp_feature` VALUES (1,'Create an account','Create an account and chose currently released trackable features from profile page, add logs starting with the week, then day then any features chosen to track from profile (water always on)'),(2,'Water Tracking','Ability to track the amount of water consumed each day'),(3,'Medication','Able to add a medication you took from the bank of previously saved (by any user) medications. (Medication names are all that are saved in the bank'),(4,'Mood','Able to log your mood at that moment and through out the day as well as add any symptoms related to your mood.  Symptoms are in a bank of different ones added by any user'),(5,'Fitness','Track how often, how long and, what you do for work outs'),(6,'Weather','Will log the current pressure for your current zip code.  This is used more to help find patterns that can happend due to weather changes'),(7,'Work','Logging of computer time hours or general work hours to help show patterns.'),(8,'Diabetic','Keep track of your sugar levels.'),(9,'Food','Keep a log of what foods are consumed'),(10,'Journal','A written log of what happened any given day.  1 per day but update able'),(11,'Sleep','Log when you fell alseep vs when you woke up.  Comments for any sleep trackers used to add more data'),(12,'Chat App','Talke to fellow Geeks about what is going on.  As more features are released will also enable user to interact with a Mentor'),(13,'PDF','Generate and print the last x number of logs for your provider.'),(14,'Provider Access','Will enable the user to invite their provider to create an account (both general user and provider side will be avaiilable to them) so they can skip the pdf'),(15,'Training','Mentor training section'),(16,'CSS','Updates to CSS for general desktop as well as Mobile Friendly'),(17,'Messaging','Messaging between user and provider for quick updates'),(18,'Alerts','Both in app and email alerts when a message is received or for providers when certiain criteria is met'),(19,'Mobile App','OS and Android compatable application');
/*!40000 ALTER TABLE `coreApp_feature` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-07 22:58:59
