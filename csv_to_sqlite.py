#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:07:16 2024
@author: maalal
"""
import pandas as pd
import sqlite3

#Creating panda variable from each CSV

circuits = pd.read_csv('Ergast_DB/f1db_csv/circuits.csv')
constructor_results = pd.read_csv('Ergast_DB/f1db_csv/constructor_results.csv')
constructor_standings = pd.read_csv('Ergast_DB/f1db_csv/constructor_standings.csv')
constructors = pd.read_csv('Ergast_DB/f1db_csv/constructors.csv')
driver_standings = pd.read_csv('Ergast_DB/f1db_csv/driver_standings.csv')
drivers = pd.read_csv('Ergast_DB/f1db_csv/drivers.csv')
lap_times = pd.read_csv('Ergast_DB/f1db_csv/lap_times.csv')
pit_stops = pd.read_csv('Ergast_DB/f1db_csv/pit_stops.csv')
qualifying = pd.read_csv('Ergast_DB/f1db_csv/qualifying.csv')
races = pd.read_csv('Ergast_DB/f1db_csv/races.csv')
results = pd.read_csv('Ergast_DB/f1db_csv/results.csv')
seasons = pd.read_csv('Ergast_DB/f1db_csv/seasons.csv')
sprint_results = pd.read_csv('Ergast_DB/f1db_csv/sprint_results.csv')
status = pd.read_csv('Ergast_DB/f1db_csv/status.csv')

#Starting sqlite DB
f1_db = sqlite3.connect('sqlite_DB/f1db_sqlite.db')
cursor = f1_db.cursor()

#Importing circuits panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS circuits(
circuitId, circuitRef, name, location, country, lat, lng, alt, url)'''

cursor.execute(create_table)

circuits.to_sql('circuits', f1_db,if_exists='replace', index=False)

#Importing constructor_results panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS constructor_results(
constructorResultsId, raceId, constructorId, points, status)'''

cursor.execute(create_table)

constructor_results.to_sql('constructor_results', f1_db,if_exists='replace', index=False)

#Importing constructor_standings panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS constructor_standings(
constructorStandingsId, raceId, constructorId, points, position, positionText, wins)'''

cursor.execute(create_table)

constructor_standings.to_sql('constructor_standings', f1_db,if_exists='replace', index=False)

#Importing constructors panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS constructors(
constructorId, constructorRef, name, nationality, url)'''

cursor.execute(create_table)

constructors.to_sql('constructors', f1_db,if_exists='replace', index=False)

#Importing driver_standings panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS driver_standings(
driverStandingsId, raceId, driverId, points, position, positionText, wins)'''

cursor.execute(create_table)

driver_standings.to_sql('driver_standings', f1_db,if_exists='replace', index=False)

#Importing drivers panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS drivers(
driverId, driverRef, number, code, forename, surname, dob, nationality, url)'''

cursor.execute(create_table)

drivers.to_sql('drivers', f1_db,if_exists='replace', index=False)

#Importing lap_times panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS lap_times(
raceId, driverId, lap, position, time, milliseconds)'''

cursor.execute(create_table)

lap_times.to_sql('lap_times', f1_db,if_exists='replace', index=False)

#Importing pit_stops panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS pit_stops(
raceId, driverId, stop, lap, time, duration, milliseconds)'''

cursor.execute(create_table)

pit_stops.to_sql('pit_stops', f1_db,if_exists='replace', index=False)

#Importing qualifying panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS qualifying(
qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3)'''

cursor.execute(create_table)

qualifying.to_sql('qualifying', f1_db,if_exists='replace', index=False)

#Importing races panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS races(
raceId, year, round, circuitId, name, date, time, url, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time)'''

cursor.execute(create_table)

races.to_sql('races', f1_db,if_exists='replace', index=False)

#Importing results panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS results(
resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId)'''

cursor.execute(create_table)

results.to_sql('results', f1_db,if_exists='replace', index=False)

#Importing seasons panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS seasons(
year, url)'''

cursor.execute(create_table)

seasons.to_sql('seasons', f1_db,if_exists='replace', index=False)

#Importing sprint_results panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS sprint_results(
resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, fastestLapTime, statusId)'''

cursor.execute(create_table)

sprint_results.to_sql('sprint_results', f1_db,if_exists='replace', index=False)

#Importing status panda variable to sqlite DB
create_table = '''CREATE TABLE IF NOT EXISTS status(
statusId, status)'''

cursor.execute(create_table)

status.to_sql('status', f1_db,if_exists='replace', index=False)