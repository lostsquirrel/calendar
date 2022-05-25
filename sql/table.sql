CREATE TABLE `calendar`.`users`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `modified_time` datetime NOT NULL,
  `state` int NOT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE `calendar`.`user_info`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` int UNSIGNED NOT NULL,
  `pregnancy` int NOT NULL,
  `menstruation_period` int NOT NULL,
  `full_period` int NOT NULL,
  `create_time` datetime NOT NULL,
  `modified_time` datetime NOT NULL,
  `state` int NOT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE `calendar`.`token`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `token` char(32) NOT NULL,
  `user_id` int UNSIGNED NOT NULL,
  `create_time` datetime NOT NULL,
  `modified_time` datetime NOT NULL,
  `state` int NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `calendar`.`calendar` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `user_id` int UNSIGNED NOT NULL,
  `create_time` datetime NOT NULL,
  `modified_time` datetime NOT NULL,
  `state` int NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `calendar`.`events` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` varchar(2000) NOT NULL,
  `calendar_id` int UNSIGNED NOT NULL,
  `create_time` datetime NOT NULL,
  `modified_time` datetime NOT NULL,
  `state` int NOT NULL,
  PRIMARY KEY (`id`)
);
