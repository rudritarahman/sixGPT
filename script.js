$(document).ready(function () {
  function getData() {
    $.get("http://localhost:3000", function (data) {
      var html = "";
      for (var i = 0; i < data.length; i++) {
        //A lot of formatting starts here

        var datetimeString = data[i].timestamp;

        // Split the datetime string into date and time substrings
        var datetimeArray = datetimeString.split(" ");
        var dateString = datetimeArray[0];
        var timeString = datetimeArray[1];

        //Make dd/mm/yyyy
        // Split the date string into year, month, and day substrings
        var dateArray = dateString.split("-");
        var year = dateArray[0];
        var month = dateArray[1];
        var day = dateArray[2];

        // Rearrange the substrings into the desired format and concatenate them with "/"
        var dateString = day + "/" + month + "/" + year;

        //main code for html work

        html += "<div style='border: 1px solid black; padding: 10px;'>";
        html += "<p>Date: " + dateString + "</p>";
        html += "<p>Time: " + timeString + "</p>";
        html += "<p>Temperature: " + data[i].temperature + " C </p>";
        html += "<p>Humidity: " + data[i].humidity + "%</p>";
        html += "<p>Methane Emission: " + data[i].methane + " ml </p>";
        html += "</div>";
      }
      $("#data").html(html);
    });
  }

  // Call the getData function initially to populate the data
  getData();

  // Set an interval to call the getData function every second
  setInterval(getData, 1000);
});
