-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/

DROP TABLE IF EXISTS hostel_travel;
DROP TABLE IF EXISTS latitude_longitude;
DROP TABLE IF EXISTS country_travel;

CREATE TABLE country_travel (
    country_name VARCHAR(100)   NOT NULL,
    country_code VARCHAR(2)   NOT NULL,
    country_desc VARCHAR   NOT NULL,
    embassy_consulate_usa VARCHAR   NOT NULL,
    entry_exit_requirements VARCHAR   NOT NULL,
    laws_circumstances VARCHAR   NOT NULL,
    safety_and_security VARCHAR   NOT NULL,
    health_circumstances VARCHAR   NOT NULL,
    CONSTRAINT pk_country_travel PRIMARY KEY (
        country_name
     )
);

CREATE TABLE hostel_travel (
	id SERIAL   NOT NULL,
    country_name VARCHAR(100)   NOT NULL,
    city_name VARCHAR(100)   NOT NULL,
    hostel_name VARCHAR(100)   NOT NULL,
    local_currency VARCHAR(3)   NOT NULL,
    rank VARCHAR(2)   NOT NULL,
    total_cost FLOAT   NOT NULL,
    attractions_cost FLOAT   NOT NULL,
    per_night_hostel FLOAT   NOT NULL,
    drinks_entertainment FLOAT   NOT NULL,
    meals FLOAT   NOT NULL,
    transportation FLOAT   NOT NULL,
    CONSTRAINT pk_hostel_travel PRIMARY KEY (
        id
     )
);

CREATE TABLE latitude_longitude (
	id SERIAL   NOT NULL,
    country_name VARCHAR(100)   NOT NULL,
    city_name VARCHAR(100)   NOT NULL,
    latitude FLOAT   NOT NULL,
    longitude FLOAT   NOT NULL,
    CONSTRAINT pk_latitude_longitude PRIMARY KEY (
        id
     )
);

ALTER TABLE hostel_travel ADD CONSTRAINT fk_hostel_travel_country FOREIGN KEY(country_name) REFERENCES country_travel (country_name);
ALTER TABLE latitude_longitude ADD CONSTRAINT fk_latitude_longitude_country FOREIGN KEY(country_name) REFERENCES country_travel (country_name);

