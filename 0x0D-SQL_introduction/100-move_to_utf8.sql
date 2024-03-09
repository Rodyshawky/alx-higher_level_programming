-- Change character SET and COLLATE
-- cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
USE hbtn_0c_0
 CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,\n  `score` int DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
