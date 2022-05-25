CREATE DATABASE `calendar` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci';

CREATE USER `calendar`@`%` IDENTIFIED BY 'calendar123';

GRANT Alter, Alter Routine, Create, Create Routine, Create Temporary Tables, Create View, Delete, Drop, Event, Execute, Grant Option, Index, Insert, Lock Tables, References, Select, Show View, Trigger, Update ON `calendar`.* TO `calendar`@`%`;