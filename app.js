// Load the required modules
const express = require("express");
const sqlite3 = require("sqlite3").verbose();

// Create a new instance of the Express application
const app = express();

// Define the port number to listen on
const port = 3000;

// Open a connection to the database
const db = new sqlite3.Database("./sensor_data.db");

// Define the route to display the data from the sensor_data table
app.get("/", (req, res) => {
  const sql =
    "SELECT timestamp, temperature, humidity, methane FROM sensor_data";
  db.all(sql, [], (err, rows) => {
    if (err) {
      return console.error(err.message);
    }
    res.setHeader("Access-Control-Allow-Origin", "*"); // Allow cross-origin requests
    res.send(rows);
  });
});

// Start listening on the specified port
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
