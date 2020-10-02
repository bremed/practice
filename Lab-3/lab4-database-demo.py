import sqlite3


dbconnect = sqlite3.connect("mydatabase.db");

dbconnect.row_factory = sqlite3.Row;

cursor = dbconnect.cursor();

cursor.execute('SELECT * FROM sensors WHERE zone = "kitchen"');
print("Kitchen Sensors:");
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);

cursor.execute('SELECT * FROM sensors WHERE type = "door"');
print("Door type Sensors:");
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);
dbconnect.close();