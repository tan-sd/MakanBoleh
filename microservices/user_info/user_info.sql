CREATE DATABASE IF NOT EXISTS `user_info` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `user_info`;

DROP TABLE IF EXISTS `user_info`;
CREATE TABLE IF NOT EXISTS `user_info` (
  `user_id` int(11) NOT NULL auto_increment,
  `name` varchar(64) NOT NULL,
  `address` varchar(64) NOT NULL,
  `latitude` decimal(10,6) ,
  `longitude` decimal(10,6) ,
  `dietary_type` varchar(64) ,
  `travel_appetite` varchar(64) ,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user_info`
--

INSERT INTO `user_info` (`name`, `address`, `latitude`,`longitude`,`dietary_type`, `travel_appetite`) 
VALUES
('ShengJingBing', 'Singapore Marina Bay Sands', 1.283375, 103.860725 , 'na', 'far'),
('DancerAdam', 'Singapore Management University', 41.023472, -91.967133 , 'na', 'far');
COMMIT;

SELECT * FROM user_info;