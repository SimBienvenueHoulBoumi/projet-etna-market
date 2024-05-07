CREATE TABLE `Products` (
  `id` integer PRIMARY KEY,
  `name` VARCHAR(255),
  `detail` VARCHAR(255),
  `userID` VARCHAR(255),
  `quantity` INTEGER,
  `createAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updateAt` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE `Products` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
