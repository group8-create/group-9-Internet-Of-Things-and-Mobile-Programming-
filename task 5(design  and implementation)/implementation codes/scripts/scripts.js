// Instance 2
var i2 = 0;
var j2 = 0;
var txts2 =["The system optimizes routes for efficient travel, saving time and simplifying journeys.","By reducing waiting time and streamlining travel routes, the system enhances user satisfaction and creates a seamless experience.", "Passengers enjoy ease and convenience with optimized routes and real-time updates, ensuring smooth transitions during their hassle-free journeys."] 
var speed2 = 100;
var del =1;
function typeWriter2() {
  if (i2 < txts2[j2].length) {
    document.getElementById("element2").innerHTML += txts2[j2].charAt(i2);
    i2++;
    setTimeout(typeWriter2, speed2);
  } else {
    setTimeout(deleteText2, speed2);
  }
}

function deleteText2() {
  if (i2 > 0) {
    var text = document.getElementById("element2").innerHTML;
    document.getElementById("element2").innerHTML = text.slice(0, -1);
    i2--;
    setTimeout(deleteText2, del);
  } else {
    j2 = (j2 + 1) % txts2.length;
    setTimeout(typeWriter2, del);
  }
}

typeWriter2()


    function displayWords(words) {
      var container = document.getElementById('word-container');
      var delay = 0;

      function removeWord(wordElement) {
        wordElement.classList.add('fade-out');

        setTimeout(function() {
          container.removeChild(wordElement);
        }, 1000); // Delay to remove the word after the fade-out animation is complete
      }

      function showNextWord() {
        if (words.length === 0) {
          // If all words have been displayed, restart the process
          words = ['Businesses ', 'Employess', 'Teachers',"Ceo's","students","Tourist","NKD","Disabled",'Vips', 'Customers'];
        }

        var word = words.shift(); // Get the next word from the list
        var wordElement = document.createElement('div');
        wordElement.classList.add('word');
        wordElement.textContent = word;

        container.appendChild(wordElement);

        setTimeout(function() {
          removeWord(wordElement);
        }, delay);

        delay = 2000; // Delay in milliseconds between each word

        setTimeout(showNextWord, delay);
      }

      // Start the process
      showNextWord();
    }

    // Example usage
    var wordsList = ['Businesses ', 'Employess', 'Teachers',"Ceo's","students","Tourist","NKD","Disabled",'Vips', 'Customers'];
    displayWords(wordsList);
// --------------------------------------login----------------------------------------------------------------
function showLoginPopup() {
  document.getElementById('loginPopup').style.display = 'flex';
}

// --------------------------------------------------------------signup---------------------------------------------------------------- 
function showSignupPopup() {
  document.getElementById('signupPopup').style.display = 'flex';
}

function hideSignupPopup() {
  document.getElementById('signupPopup').style.display = 'none';
}
// ---------------------------------------------------------map----------------------------------------------------------
function initMap() {
  // Check if Geolocation is supported by the browser
  if (navigator.geolocation) {
    // Get the user's current location
    navigator.geolocation.getCurrentPosition(
      function(position) {
        // Get the latitude and longitude
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;

        // Set the coordinates for the initial map center
        var myLatLng = { lat: lat, lng: lng };

        // Create a map object and specify the element to display it
        var map = new google.maps.Map(document.getElementById("map"), {
          center: myLatLng,
          zoom: 12 // Adjust the zoom level as desired
        });

        // Add a marker to the map
        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: "Current Location" // Replace with your desired marker title
        });
      },
      function(error) {
        console.error("Error getting current location:", error);
      }
    );
  } else {
    console.error("Geolocation is not supported by this browser.");
  }
}