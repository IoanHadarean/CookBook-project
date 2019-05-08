-- MySQL dump 10.13  Distrib 5.5.57, for debian-linux-gnu (x86_64)
--
-- Host: 0.0.0.0    Database: flaskapp
-- ------------------------------------------------------
-- Server version	5.5.57-0ubuntu0.14.04.1

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
-- Table structure for table `userRatings`
--

DROP TABLE IF EXISTS `userRatings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userRatings` (
  `userId` int(11) DEFAULT NULL,
  `recipeId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userRatings`
--

LOCK TABLES `userRatings` WRITE;
/*!40000 ALTER TABLE `userRatings` DISABLE KEYS */;
/*!40000 ALTER TABLE `userRatings` ENABLE KEYS */;
UNLOCK TABLES;

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
  `unliked` int(11) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlikes`
--

LOCK TABLES `userlikes` WRITE;
/*!40000 ALTER TABLE `userlikes` DISABLE KEYS */;
INSERT INTO `userlikes` VALUES (1,2,0,1),(1,3,0,1),(1,1,0,1),(78,2,0,1),(78,3,1,0),(78,1,0,1),(79,6,1,0),(1,5,0,1),(80,1,0,1),(79,5,0,1),(81,5,0,1),(81,2,0,1),(81,3,0,1),(80,2,0,1),(79,2,0,1),(80,3,0,1),(80,6,0,1),(80,5,0,1),(80,4,1,0),(80,8,0,1),(80,7,1,0),(1,4,1,0),(1,12,0,1),(78,12,0,1),(80,12,0,1),(80,9,1,0),(1,6,1,0),(79,1,0,1),(80,22,0,1),(92,1,0,1),(93,1,0,1),(93,2,0,1),(94,2,0,1),(93,5,1,0),(99,3,1,0),(100,19,1,0),(99,18,0,1),(101,2,0,1),(101,1,0,1),(84,1,0,1),(84,3,0,1),(84,2,1,0),(84,6,0,1),(80,11,1,0),(80,10,1,0),(102,1,1,0),(84,4,1,0),(84,11,0,1),(103,2,0,1),(103,1,0,1),(103,3,0,1),(84,12,1,0),(84,21,1,0);
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
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'ggggggggggg','f@id.comffsssssssssss','testuser','$5$rounds=535000$AVGRf9EriSja3YCI$IQI/FAp1uoJIOLWis/yKLH.h5LXL4p2yqEwbvIxFou/','2019-03-29 01:44:41',0,NULL,'avatar.jpg'),(78,'Ioan-Dumitru Hadarean','hadareannelutu@yahoo.com','goagl111','$5$rounds=535000$fUUNpWfiOnHJdDlD$wXfBrrmpl3sA1tVwJ9CrBj0q521Aw7xQZGnOzkRcas9','2019-03-27 15:57:15',0,NULL,'avatar.jpg'),(79,'Andreea','andreea_pastiu99@yahoo.com','deea99','$5$rounds=535000$g2sbU4ZdjfO9U1tp$dP5.65lkf/PXIulyq.Hpn/hcBZssJTAkEo6WEFkbfHD','2019-03-28 15:58:22',0,NULL,'avatar.jpg'),(80,'Moosa Hassan','moosa_mentor@yahoo.com','moosa111','$5$rounds=535000$LasF.hknPyxdlROd$LOl7nmJy5MEzBwRepHxofnQRVmQ1vAGon0/OzlazCOA','2019-03-28 23:39:37',0,'Hello, I am a mentor at Code Institute.','oDKvNzSzTF9jgcoNKYVJpw==.png'),(81,'m123456','m123456@m123456.com','m123456','$5$rounds=535000$40mroBcMjHEmoR18$V/h9fsI1wod15jLLtjowMsMnNOWi.WawdXw56GXHQG0','2019-03-31 14:44:11',0,NULL,'avatar.jpg'),(82,'Torgny Engström','torgny.engstrom@gmail.com','adminadmin','$5$rounds=535000$qEDvmXEFY75w0rQx$e2J5Y2tbOMbVH9DbyjUTTMDo3g2XR0/Kn2RKslfl2f3','2019-03-31 18:56:14',0,NULL,'avatar.jpg'),(83,'Ioan','sfdsfdsfdsfd@yahoo.com','goagl11111111','$5$rounds=535000$UUfu83R8KbSh6Y.x$hF1lsGz407YLU/0lNOD3zrHGI.Ar6qL9gLhBbYo8l05','2019-04-02 08:20:25',0,NULL,'avatar.jpg'),(84,'Andreeea','ioan123@yahoo.com','Ioan-Dumitru Hadarean','$5$rounds=535000$IQeSTMCxR57As.j7$vp4dhUB3TtF6VT2imxYowfYsHHwIBSm13p0v/3jkFo5','2019-04-06 20:58:01',0,'aaaaaaaaaaaaaaaaaaaaaa','5GzZCYcMsldYTkVI0dgJvg==.png'),(98,'Ioan123','ioan34@yahoo.com','goagl1403','$5$rounds=535000$R.Mqrbr6ppA9suUX$uxtZk/CNJtwKM6kBuyODBIpWWfdlf0C.O0xlQa05mX5','2019-04-12 15:20:22',0,NULL,'avatar.jpg'),(99,'ioan456','ioan123456@yahoo.com','daddasdasdasdasdasdas','$5$rounds=535000$zHonQAANLr8HRiFS$q0ofntYC6KyCDzg.YydbI6rD2LPTfiSt0TsKHgXMCx0','2019-04-12 15:22:45',0,'dsadddddddddddddddddddddddddd','jQ7nPAZi+PMQA3K|rfbDgg==.jpg'),(100,'Gheorghe Pascu','tudorpascu787@gmail.com','gigifon','$5$rounds=535000$EZlXaLHcHXN/Tlk7$BBz.TtdIHgsqhL37nKm4mooOiNvznxP2arJLcMo0J65','2019-04-13 20:47:27',0,NULL,'avatar.jpg'),(101,'I love pancakes','pancakes@email.com','hmmm thinking','$5$rounds=535000$Vat.BWSNouvDeEy2$sGu.Qi504fF51fZKyR7ljhXCbXDy1V/ruZgMnO8HrfA','2019-04-17 19:00:05',0,'Hello, I love pancakes','EyxZ|zKTfPm1d3jpwvRsWQ==.png'),(102,'Moosa Hassan','Iampenta@yahoo.com','I am Penta','$5$rounds=535000$AYzyJlBC/OGPxP2y$ee2fM9dy/Obg5Qj.IbYGj9fO/HduvRn7k4/435V0BY/','2019-05-02 15:31:41',0,NULL,'avatar.jpg'),(103,'Miroslav','loil.engstrom@gmail.com','Mirorow','$5$rounds=535000$Irlr4.7lv2yYXQw.$rkHvwMjO1j/Q75PX9E919AVTfDxxXnKmGRA2l8pClR3','2019-05-03 15:19:04',0,NULL,'avatar.jpg');
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

-- Dump completed on 2019-05-08  9:48:50
