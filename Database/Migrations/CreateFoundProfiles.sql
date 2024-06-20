CREATE TABLE `found_profiles` (
	`id` VARCHAR(32) PRIMARY KEY,
    `website_id` VARCHAR(32) NOT NULL, 
    `username` VARCHAR(255) NOT NULL,
	`url` VARCHAR(255) NOT NULL,
	`date_created` INT DEFAULT 0,

    FOREIGN KEY (`website_id`) REFERENCES website_urls (`id`)
);