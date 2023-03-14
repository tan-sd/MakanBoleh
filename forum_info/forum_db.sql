-- this is the database setup file
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `food_db`
--
DROP DATABASE IF EXISTS `forum_db`;
CREATE DATABASE IF NOT EXISTS `forum_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `forum_db`;

-- --------------------------------------------------------

-- Table structure for table `forum_table` in database `forum_db`

DROP TABLE IF EXISTS `forum_table`;
CREATE TABLE IF NOT EXISTS `forum_table` (
  
  `forum_id` int(11) NOT NULL auto_increment,
  `username` int(11) NOT NULL,
  `title` varchar(60),
  `description` varchar(1000) NULL,
  `datetime` datetime,

  PRIMARY KEY (`forum_id`)
);