// Instance 2
var i2 = 0;
var j2 = 0;
var speed2 = 100;
var del = 1;

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
            words = ['Businesses ', 'Employess', 'Teachers', "Ceo's", "students", "Tourist", "NKD", "Disabled", 'Vips', 'Customers'];
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
var wordsList = ['Businesses ', 'Employess', 'Teachers', "Ceo's", "students", "Tourist", "Disabled", 'Vips', 'Customers'];
displayWords(wordsList);
// --------------------------------------login----------------------------------------------------------------
function showLoginPopup() {
    document.getElementById('loginPopup').style.display = 'flex';
}

// --------------------------------------Forgot password----------------------------------------------------------------
function showForgotPasswordPopup() {
    document.getElementById('forgotpasswordPopup').style.display = 'flex';
}


// --------------------------------------------------------------signup---------------------------------------------------------------- 
function showSignupPopup() {
    document.getElementById('signupPopup').style.display = 'flex';
}

function hideSignupPopup() {
    document.getElementById('signupPopup').style.display = 'none';
}
// ---------------------------------------------------------map_driver- ---------------------------------------------------------
function initMap() {
    let destinationMarker = null;
    let directionsRenderer = null;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    } else {
        alert('Geolocation is not supported by this browser.');
    }

    function successCallback(position) {
        const passengerLocation = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        const map = new google.maps.Map(document.getElementById('map'), {
            center: passengerLocation,
            zoom: 15
        });

        const marker = new google.maps.Marker({
            position: passengerLocation,
            map: map,
            title: 'Passenger Current Location'
        });

        // Add click event listener to the map
        map.addListener('click', function(event) {
            // Remove previous destination marker and route
            if (destinationMarker) {
                destinationMarker.setMap(null);
            }
            if (directionsRenderer) {
                directionsRenderer.setMap(null);
            }

            const destinationLocation = event.latLng;

            // Add a marker for the destination location
            destinationMarker = new google.maps.Marker({
                position: destinationLocation,
                map: map,
                title: 'Destination'
            });

            // Draw a route from passenger location to the destination
            const directionsService = new google.maps.DirectionsService();
            directionsRenderer = new google.maps.DirectionsRenderer();
            directionsRenderer.setMap(map);
            const request = {
                origin: passengerLocation,
                destination: destinationLocation,
                travelMode: google.maps.TravelMode.DRIVING
            };
            directionsService.route(request, function(response, status) {
                if (status === google.maps.DirectionsStatus.OK) {
                    directionsRenderer.setDirections(response);
                }
            });
        });
    }

    function errorCallback(error) {
        alert('Error retrieving current location: ' + error.message);
    }
}


// $(document).ready(function() {
//   $('#sidebarCollapse').on('click', function() {
//       $('#sidebar').toggleClass('active');
//       $('#content').toggleClass('active');
//   });
//   });
// -----------------------------------------------------side bar
$(document).ready(function() {
    var screenWidth = $(window).width();
    var sidebar = $('#sidebar');
    var content = $('#content');

    if (screenWidth >= 768) {
        sidebar.removeClass('active'); // Hide the sidebar on desktop screens
        content.removeClass('active');
    }

    $(window).scroll(function() {
        if (screenWidth < 768) {
            sidebar.removeClass('active');
            content.removeClass('active');
        }
    });

    $('#sidebarCollapse').on('click', function() {
        sidebar.toggleClass('active');
        content.toggleClass('active');
    });
});