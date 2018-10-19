-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: sailors2
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

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
-- Table structure for table `boats`
--

DROP TABLE IF EXISTS `boats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boats` (
  `bid` int(11) NOT NULL,
  `eid` int(11) DEFAULT NULL,
  `bname` char(20) DEFAULT NULL,
  `color` char(10) DEFAULT NULL,
  `length` int(11) DEFAULT NULL,
  `wear` int(11) DEFAULT NULL,
  `rent` int(11) DEFAULT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boats`
--

LOCK TABLES `boats` WRITE;
/*!40000 ALTER TABLE `boats` DISABLE KEYS */;
INSERT INTO `boats` VALUES (101,1,'Interlake','blue',45,50,100),(102,3,'Interlake','red',45,50,100),(103,4,'Clipper','green',40,20,100),(104,2,'Clipper','red',40,20,100),(105,1,'Marine','red',35,20,90),(106,3,'Marine','green',35,20,90),(107,4,'Marine','blue',35,20,90),(108,2,'Driftwood','red',35,20,90),(109,1,'Driftwood','blue',35,20,90),(110,3,'Klapser','red',30,80,90),(111,4,'Sooney','gren',28,80,80),(112,2,'Sooney','red',28,80,80);
/*!40000 ALTER TABLE `boats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `eid` int(11) NOT NULL,
  `ename` varchar(30) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `employment_duration` int(11) DEFAULT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Schapiro',300,4),(2,'Jennifer',200,3),(3,'Euguene',500,5),(4,'Scott',100,1);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserves`
--

DROP TABLE IF EXISTS `reserves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reserves` (
  `sid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `day` date NOT NULL,
  `start_d` date DEFAULT NULL,
  `return_d` date DEFAULT NULL,
  PRIMARY KEY (`sid`,`bid`,`day`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserves`
--

LOCK TABLES `reserves` WRITE;
/*!40000 ALTER TABLE `reserves` DISABLE KEYS */;
INSERT INTO `reserves` VALUES (22,101,'1998-10-10','1998-12-15','1998-12-16'),(22,102,'1998-10-10','1998-12-17','1998-12-20'),(22,103,'1998-08-10','1998-12-21','1998-12-23'),(22,104,'1998-07-10','1998-12-24','1998-12-31'),(23,104,'1998-10-10','1998-12-24','1998-12-31'),(23,105,'1998-11-10','1998-12-15','1998-12-31'),(24,104,'1998-10-10','1998-12-15','1998-12-31'),(31,102,'1998-11-10','1998-12-15','1998-12-31'),(31,103,'1998-11-06','1998-12-15','1998-12-31'),(31,104,'1998-11-12','1998-12-15','1998-12-31'),(35,104,'1998-08-10','1998-12-15','1998-12-31'),(35,105,'1998-11-06','1998-12-15','1998-12-31'),(59,105,'1998-07-10','1998-12-10','1998-12-31'),(59,106,'1998-11-12','1998-12-10','1998-12-31'),(59,109,'1998-11-10','1998-12-10','1998-12-31'),(60,106,'1998-09-05','1998-12-10','1998-12-31'),(60,106,'1998-09-08','1998-12-10','1998-12-31'),(60,109,'1998-07-10','1998-12-10','1998-12-31'),(61,112,'1998-09-08','1998-12-25','1998-12-31'),(62,110,'1998-11-06','1998-12-10','1998-12-31'),(64,101,'1998-09-05','1998-12-10','1998-12-31'),(64,102,'1998-09-08','1998-12-10','1998-12-31'),(74,103,'1998-09-08','1998-12-20','1998-12-31'),(88,107,'1998-09-08','1998-12-20','1998-12-31'),(88,110,'1998-09-05','1998-12-20','1998-12-31'),(88,110,'1998-11-12','1998-12-20','1998-12-31'),(88,111,'1998-09-08','1998-12-25','1998-12-31'),(89,108,'1998-10-10','1998-12-20','1998-12-31'),(89,109,'1998-08-10','1998-12-20','1998-12-31'),(90,109,'1998-10-10','1998-12-20','1998-12-31');
/*!40000 ALTER TABLE `reserves` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sailors`
--

DROP TABLE IF EXISTS `sailors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sailors` (
  `sid` int(11) NOT NULL,
  `sname` varchar(30) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sailors`
--

LOCK TABLES `sailors` WRITE;
/*!40000 ALTER TABLE `sailors` DISABLE KEYS */;
INSERT INTO `sailors` VALUES (22,'dusting',7,45),(23,'emilio',7,45),(24,'scruntus',1,33),(29,'brutus',1,33),(31,'lubber',8,56),(32,'andy',8,26),(35,'figaro',8,56),(58,'rusty',10,35),(59,'stum',8,26),(60,'jit',10,35),(61,'ossola',7,16),(62,'shaun',10,35),(64,'horatio',7,16),(71,'zorba',10,35),(74,'horatio',9,26),(85,'art',3,26),(88,'dan',9,26),(89,'dye',3,26),(90,'vin',3,64),(95,'bob',3,64);
/*!40000 ALTER TABLE `sailors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-18 14:40:21
