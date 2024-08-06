CREATE TABLE weather_data(
	Date_Time DATE,
	Temp_C VARCHAR(50),
	Dew_Point_Temp_C VARCHAR(50),
	Rel_Hum_value VARCHAR(50),
    Wind_Speed_km_h VARCHAR(50),
	Visibility_km VARCHAR(50),
	Press_kPa VARCHAR(50),
	Weather_condition VARCHAR(50)
	);

COPY weather_data(Date_Time, Temp_C, Dew_Point_Temp_C, Rel_Hum_value, Wind_Speed_km_h, Visibility_km, Press_kPa, Weather_condition)
FROM '/Users/apple/Desktop/Weather_Data.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM weather_data;

-- 1. Select all the records where the weather was exactly clear
SELECT * FROM weather_data
WHERE weather_condition = 'Clear';

--2. Find the number of times the wind speed was exactly 4km/h
-- used varchar and the numbers are treated as string
SELECT COUNT(wind_speed_km_h)
FROM weather_data
WHERE wind_speed_km_h='4';

--3. check if there are null values in the dataset
SELECT COUNT(*)
FROM weather_data
WHERE wind_speed_km_h = ISNULL;

-- 4. Rename the column

ALTER TABLE weather_data
RENAME COLUMN Weather_condition, Weather_Condition;