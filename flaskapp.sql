-- MySQL dump 10.13  Distrib 5.5.57, for debian-linux-gnu (x86_64)
--
-- Host: wyqk6x041tfxg39e.chr7pe7iynqr.eu-west-1.rds.amazonaws.com    Database: rg0qy5ylfuoz0084
-- ------------------------------------------------------
-- Server version	5.7.23-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `userlikes`
--

DROP TABLE IF EXISTS `userlikes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlikes` (
  `userId` int(11) DEFAULT NULL,
  `recipeId` int(11) DEFAULT NULL,
  `liked` int(11) DEFAULT '1',
  `unliked` int(11) DEFAULT '1',
  `count_liked` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlikes`
--

LOCK TABLES `userlikes` WRITE;
/*!40000 ALTER TABLE `userlikes` DISABLE KEYS */;
INSERT INTO `userlikes` VALUES (117,1,0,1,1),(116,1,0,1,1),(118,1,0,1,1),(118,9,1,1,0),(118,2,1,1,0),(118,11,1,1,0),(120,1,1,0,1),(120,2,0,1,1),(120,3,1,1,0),(120,5,1,0,1),(118,5,0,1,1),(121,5,0,1,1),(118,6,1,1,0),(117,6,1,1,0),(121,6,1,1,0),(121,2,1,1,0),(121,4,1,1,0),(118,4,1,1,0),(121,1,0,1,1);
/*!40000 ALTER TABLE `userlikes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `register_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `likes` int(11) NOT NULL,
  `aboutme` varchar(140) DEFAULT NULL,
  `image` varchar(255) DEFAULT 'avatar.jpg',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (116,'Andreeea','ioan123@yahoo.com','Andreea','$5$rounds=535000$AiflOhLiL2zrQ9RU$hujhaEaAX5Un5tZy0yQmYuW3cUib6V5CxaYWQw.G3c8','2019-05-16 21:59:03',0,NULL,'avatar.jpg'),(117,'Moosa Hassan','moosa_mentor@yahoo.com','moosa111','$5$rounds=535000$9pTNU7X74ewMQzy8$CbFBLNQ0CydVlcA4rwST/5BbzVkEystvJdprrPz3dv6','2019-05-16 22:04:20',0,NULL,'avatar.jpg'),(118,'Ioan-Dumitru Hadarean','hadareannelutu@yahoo.com','Ioan-Dumitru Hadarean','$5$rounds=535000$0Swl6sUBo5eiUraC$sR1fqcydWoZeGalhKGhhuaPvdnFfFV3GeFNnx9Xvm70','2019-05-16 22:19:11',0,NULL,'avatar.jpg'),(119,'Moosa The wonder one','moosa@yahoo.com','moosa11111','$5$rounds=535000$r.jqq4VWzP.Hdcsh$H9dBNYnEuV4r4gzXoIZmhyMMdhozJ/YJRI2x8qMkR96','2019-05-16 22:24:55',0,NULL,'avatar.jpg'),(120,'usernr6','usernr6@yahoo.com','usernr6','$5$rounds=535000$MNHEqsPFFjjchBBh$5jVtm6rhaGZi466E4Z4GKTTWiCKdg7O9Z9gCzy77eS2','2019-05-18 16:53:18',0,NULL,'avatar.jpg'),(121,'usernr5','usernr5@yahoo.com','usernr5','$5$rounds=535000$7Mjo6PfBAqI88txC$6tG0Om.ehEg/ch0fs.oXpCyQhJe9vHKoq10BwAYu6t4','2019-05-18 16:56:43',0,NULL,'avatar.jpg');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-18 19:05:56
