$(document).ready(function () {
  // Function to fetch districts and facilities based on selected region and district
  function fetchData(regionId, districtId) {
    $.ajax({
      url: "{% url 'get_districts_and_facilities' %}", // URL to fetch districts and facilities
      type: "GET",
      data: {
        region_id: regionId,
        district_id: districtId,
      },
      success: function (response) {
        // Clear previous options
        $("#facility_district, #facility_name").empty();

        // Add new options for districts
        $.each(response.districts, function (index, district) {
          $("#facility_district").append(
            $("<option>", {
              value: district.id,
              text: district.district_name,
            })
          );
        });

        // Add new options for facilities
        $.each(response.facilities, function (index, facility) {
          $("#facility_name").append(
            $("<option>", {
              value: facility.id,
              text: facility.facility_name,
            })
          );
        });
      },
      error: function (xhr, errmsg, err) {
        console.log("Error:", errmsg);
        // Handle error if needed
      },
    });
  }

  // Trigger change event on region dropdown after document is ready
  $("#facility_region").trigger("change");

  // Event listener for region dropdown change
  $("#facility_region").on("change", function () {
    var selectedRegionId = $(this).val();
    var selectedDistrictId = $("#facility_district").val(); // Get selected district ID
    fetchData(selectedRegionId, selectedDistrictId);
  });

  // Event listener for district dropdown change
  $("#facility_district").on("change", function () {
    var selectedRegionId = $("#facility_region").val(); // Get selected region ID
    var selectedDistrictId = $(this).val();
    fetchData(selectedRegionId, selectedDistrictId);
  });
});

/*for selection age and date of birth*/
flatpickr("#date_of_birth", {
  dateFormat: "Y-m-d", // Set the date format
  // You can customize other options as needed
});

$(document).ready(function () {
  $("#facility_region").select2({
    placeholder: "Select a region",
    allowClear: true, // Optional: Add a clear button
  });
  $("#facility_name").select2({
    placeholder: "Select a region",
    allowClear: true, // Optional: Add a clear button
  });
  $("#facility_district").select2({
    placeholder: "Select a region",
    allowClear: true, // Optional: Add a clear button
  });
});

/*for other occupation*/
document.addEventListener("DOMContentLoaded", function () {
  // Get the occupation dropdown and other occupation input field
  const occupationDropdown = document.getElementById("occupation");
  const otherOccupationInput = document.getElementById("other_occupation");

  // Add event listener to the occupation dropdown
  occupationDropdown.addEventListener("change", function () {
    // Check if the selected value is "Other (Specify)"
    if (occupationDropdown.value === "other (specify)") {
      // Show the other occupation input field
      otherOccupationInput.style.display = "block";
    } else {
      // Hide the other occupation input field
      otherOccupationInput.style.display = "none";
    }
  });
});

/*for other Religion*/
document.addEventListener("DOMContentLoaded", function () {
  // Get the religion dropdown and other religion input field
  const religionDropdown = document.getElementById("religion");
  const otherReligionInput = document.getElementById("other_religion");

  // Add event listener to the occupation dropdown
  religionDropdown.addEventListener("change", function () {
    // Check if the selected value is "Other (Specify)"
    if (religionDropdown.value === "others (specify)") {
      // Show the other occupation input field
      otherReligionInput.style.display = "block";
    } else {
      // Hide the other occupation input field
      otherReligionInput.style.display = "none";
    }
  });
});

/*for other Ethnicity*/
document.addEventListener("DOMContentLoaded", function () {
  // Get the ethnicity dropdown and other ethnicity input field
  const ethnicityDropdown = document.getElementById("ethnicity");
  const otherEthinicityInput = document.getElementById("other_ethnicity");

  // Add event listener to the occupation dropdown
  ethnicityDropdown.addEventListener("change", function () {
    // Check if the selected value is "Other (Specify)"
    if (ethnicityDropdown.value === "others (specify)") {
      // Show the other occupation input field
      otherEthinicityInput.style.display = "block";
    } else {
      // Hide the other occupation input field
      otherEthinicityInput.style.display = "none";
    }
  });
});

/*for ANC VISITS BY PREGNANT WOMAN*/
document.addEventListener("DOMContentLoaded", function () {
  // Get the ethnicity dropdown and other ethnicity input field
  const ancDropdown = document.getElementById("anc");
  const totalAncVisitsInput = document.getElementById("total_anc_visits");
  const placeOfAncInput = document.getElementById("place_of_anc");
  const gestationalAgeInput = document.getElementById("gestational_age");

  // Add event listener to the occupation dropdown
  ancDropdown.addEventListener("change", function () {
    // Check if the selected value is "Other (Specify)"
    if (ancDropdown.value === "yes") {
      // Show the other occupation input field
      totalAncVisitsInput.style.display = "block";
      placeOfAncInput.style.display = "block";
      gestationalAgeInput.style.display = "block";
    } else {
      // Hide the other occupation input field
      totalAncVisitsInput.style.display = "none";
      placeOfAncInput.style.display = "none";
      gestationalAgeInput.style.display = "none";
    }
  });
});

function toggleFields() {
  var dobCheckbox = document.getElementById("dob_unknown");
  var dateOfBirthField = document.getElementById("date_of_birth");
  var ageField = document.getElementById("age");
  var ageLabel = document.getElementById("ageLabel");

  if (dobCheckbox.checked) {
    // Hide date of birth field and show age field
    dateOfBirthField.style.display = "none";
    ageField.style.display = "block";
    ageLabel.innerText = "Age"; // Update label text
  } else {
    // Show date of birth field and hide age field
    dateOfBirthField.style.display = "block";
    ageField.style.display = "none";
    ageLabel.innerText = "Age"; // Update label text
  }
}
