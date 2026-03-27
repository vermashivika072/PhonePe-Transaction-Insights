CREATE DATABASE IF NOT EXISTS phonepe_pulse CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE phonepe_pulse;

-- Aggregated User Table
CREATE TABLE IF NOT EXISTS aggregated_user (
    state VARCHAR(50),
    year INT,
    quarter INT,
    brand VARCHAR(50),
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    percentage DOUBLE,
    PRIMARY KEY (state, year, quarter, brand, transaction_type)
);

-- Aggregated Transaction Table
CREATE TABLE IF NOT EXISTS aggregated_transaction (
    state VARCHAR(50),
    year INT,
    quarter INT,
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    total_amount BIGINT,
    PRIMARY KEY (state, year, quarter, transaction_type)
);

-- Aggregated Insurance Table
CREATE TABLE IF NOT EXISTS aggregated_insurance (
    state VARCHAR(50),
    year INT,
    quarter INT,
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    total_amount BIGINT,
    PRIMARY KEY (state, year, quarter, transaction_type)
);

-- Map Transaction Table
CREATE TABLE IF NOT EXISTS map_transaction (
    state VARCHAR(50),
    district VARCHAR(50),
    year INT,
    quarter INT,
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    total_amount BIGINT,
    PRIMARY KEY (state, district, year, quarter, transaction_type)
);

-- Map User Table (similar structure)
CREATE TABLE IF NOT EXISTS map_user (
    state VARCHAR(50),
    district VARCHAR(50),
    year INT,
    quarter INT,
    registered_user INT,
    app_opens INT,
    PRIMARY KEY (state, district, year, quarter)
);

-- Map Insurance Table
CREATE TABLE IF NOT EXISTS map_insurance (
    state VARCHAR(50),
    district VARCHAR(50),
    year INT,
    quarter INT,
    transaction_count BIGINT,
    total_amount BIGINT,
    PRIMARY KEY (state, district, year, quarter)
);

-- Top Transaction States
CREATE TABLE IF NOT EXISTS top_transaction_states (
    state VARCHAR(50),
    year INT,
    quarter INT,
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    total_amount BIGINT,
    PRIMARY KEY (state, year, quarter, transaction_type)
);

-- Top Transaction Districts
CREATE TABLE IF NOT EXISTS top_transaction_districts (
    state VARCHAR(50),
    district VARCHAR(50),
    year INT,
    quarter INT,
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    total_amount BIGINT,
    PRIMARY KEY (state, district, year, quarter, transaction_type)
);

-- Top Transaction Pincode (subset)
CREATE TABLE IF NOT EXISTS top_transaction_pincodes (
    state VARCHAR(50),
    district VARCHAR(50),
    pincode VARCHAR(10),
    year INT,
    quarter INT,
    transaction_type VARCHAR(50),
    transaction_count BIGINT,
    total_amount BIGINT,
    PRIMARY KEY (state, district, pincode, year, quarter, transaction_type)
);
