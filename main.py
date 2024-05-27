import requests
import sqlite3
import time

def fetch_and_store_data():
    url = "http://demo.azonix.in:15080/info"
    response = requests.get(url)
    data = response.json()


    conn = sqlite3.connect('data1.db')
    c = conn.cursor()


    c.execute('''CREATE TABLE IF NOT EXISTS data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  version TEXT,
                  station_id TEXT,
                  local_ip TEXT,
                  date_time TEXT,
                  uptime TEXT,
                  relay_status TEXT,
                  station_status TEXT,
                  evse_status TEXT,
                  elapsed_time TEXT,
                  amps REAL,
                  ac_voltage INTEGER,
                  dc_voltage REAL,
                  temperature INTEGER,
                  wattage INTEGER,
                  free_heap INTEGER,
                  last_kwh REAL)''')
    print(data)


    c.execute("INSERT INTO data (version, station_id, local_ip, date_time, uptime, relay_status, station_status, evse_status, elapsed_time, amps, ac_voltage, dc_voltage, temperature, wattage, free_heap, last_kwh) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (data["Version"], data["Station_ID"], data["Local_IP"], data["Date_Time"], data["Uptime"], data["Relay_Status"], data["Station_Status"], data["EVSE_Status"], data["Elapsed_Time"], data["Amps"], data["AC_Voltage"], data["DC_Voltage"], data["Temperature"], data["Wattage"], data["Free_Heap"], data["Last_KWH"]))


    conn.commit()
    conn.close()

while True:
    fetch_and_store_data()
    time.sleep(60)