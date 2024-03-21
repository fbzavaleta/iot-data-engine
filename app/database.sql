-- Author: Francis Benjamin Zavaleta, Eng
-- Copyright © fbzavaleta. All rights reserved.

-- Check if the schema tks_engine exists
SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'tks_engine';

-- If the schema does not exist, create it along with the tables
CREATE DATABASE IF NOT EXISTS tks_engine;
USE tks_engine;

CREATE TABLE IF NOT EXISTS  engine_endpoint(
    id INT NOT NULL AUTO_INCREMENT,
    channel VARCHAR (255) NOT NULL,
    token  VARCHAR (255)  NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY channel_unique (channel)
);

CREATE TABLE IF NOT EXISTS  engine_endpoint_description (
    id INT NOT NULL AUTO_INCREMENT,
    engine_endpoint_id INT NOT NULL,
    channel_name VARCHAR (255) NOT NULL,
    latitude FLOAT,
    longitude FLOAT,
    elevation FLOAT,
    FOREIGN KEY (engine_endpoint_id) REFERENCES engine_endpoint(id),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS  engine_endpoint_description_fields (
    id INT NOT NULL AUTO_INCREMENT,
    engine_endpoint_description_id INT NOT NULL,
    field1_name VARCHAR (255),
    field2_name VARCHAR (255),
    field3_name VARCHAR (255),
    field4_name VARCHAR (255),
    field5_name VARCHAR (255),
    field6_name VARCHAR (255),
    field7_name VARCHAR (255),
    field8_name VARCHAR (255),
    FOREIGN KEY (engine_endpoint_description_id) REFERENCES engine_endpoint_description(id),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS  engine_data_sample (
    id INT NOT NULL AUTO_INCREMENT,
    engine_endpoint_id INT NOT NULL,
    entry_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    field1 FLOAT,
    field2 FLOAT,
    field3 FLOAT,
    field4 FLOAT,
    field5 FLOAT,
    field6 FLOAT,
    field7 FLOAT,
    field8 FLOAT,    
    FOREIGN KEY (engine_endpoint_id) REFERENCES engine_endpoint(id),
    PRIMARY KEY (id)
);
