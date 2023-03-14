-- this is the database setup file
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `food_db`
--
DROP DATABASE IF EXISTS `food_db`;
CREATE DATABASE IF NOT EXISTS `food_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `food_db`;

-- --------------------------------------------------------

-- Table structure for table `food_table` in database `food_db`

DROP TABLE IF EXISTS `food_table`;
CREATE TABLE IF NOT EXISTS `food_table` (
  
  `post_id` int(11) NOT NULL auto_increment,
  `creator_id` int(11) NOT NULL,
  `post_name` varchar(60),
  `latitude` decimal(10,6),
  `longitude` decimal(10,6),
  `description` varchar(1000) NULL,
  `allergens` varchar(8000) NULL, 
  `is_available` bit,

  PRIMARY KEY (`post_id`)
);

INSERT INTO `food_table` (`creator_id`, `post_name`, `latitude`, `longitude`, `description`,
 `allergens`, `is_available`) 
VALUES
( 1 ,'laichifan', 1.283125, 103.868825 , 'u broke u come', 'na', 'yes'),
( 2 ,'laichimian', 1.183195, 103.898825 , 'a lot indomee pls clear', 'na', 'yes'),
( 1 ,'di san ge', 1.283374, 103.860726, 'plain water', 'na', 'yes');
COMMIT;

SELECT * FROM food_table;