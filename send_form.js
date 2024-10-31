const steps = document.querySelectorAll(".step");
    const progressSteps = document.querySelectorAll(".progress-step");
    const progressBarFill = document.querySelector(".progress-bar-fill");

    let currentStep = 0;

    function showStep(step) {
      steps.forEach((stepElement, index) => {
        if (index === step) {
          stepElement.classList.add("active");
        } else {
          stepElement.classList.remove("active");
        }
      });

      progressSteps.forEach((progressStep, index) => {
        if (index <= step) {
          progressStep.classList.add("active");
        } else {
          progressStep.classList.remove("active");
        }
      });

      progressBarFill.style.width = ((step + 1) / steps.length) * 100 + "%";
    }

    function toggleForm() {
        var serviceType = document.getElementById('serviceType').value;
        var timeSlotDetails = document.getElementById('timeSlotDetails');
        var pickupSection = document.getElementById('pickupSection');
        var pickupTimeSection = document.getElementById('pickupTimeSection');

        if (serviceType === 'pickup_delivery') {
            // Show pick-up and delivery form
            timeSlotDetails.style.display = 'block';
            pickupSection.style.display = 'block';
            pickupTimeSection.style.display = 'block';
        } else if (serviceType === 'delivery') {
            // Show only delivery section
            timeSlotDetails.style.display = 'block';
            pickupSection.style.display = 'none';
            pickupTimeSection.style.display = 'none';
        } else {
            // Hide the form
            timeSlotDetails.style.display = 'none';
        }
    }

    document.getElementById("next1").addEventListener("click", () => {
      currentStep = 1;
      showStep(currentStep);
    });

    document.getElementById("next2").addEventListener("click", () => {
      currentStep = 2;
      showStep(currentStep);
    });

    document.getElementById("next3").addEventListener("click", () => {
      currentStep = 3;
      showStep(currentStep);
    });

    document.getElementById("prev2").addEventListener("click", () => {
      currentStep = 0;
      showStep(currentStep);
    });

    document.getElementById("prev3").addEventListener("click", () => {
      currentStep = 1;
      showStep(currentStep);
    });

    document.getElementById("prev4").addEventListener("click", () => {
      currentStep = 2;
      showStep(currentStep);
    });

    document.getElementById("submit").addEventListener("click", (e) => {
      e.preventDefault();
      
      // Show a notification to the user that the form has been submitted
      alert("Form has been submitted successfully!");

      // Display confirmation message
      document.getElementById("confirmation").style.display = "block";
      showStep(3); // Move to the final step.
    });
    const timeSlotButtons = document.querySelectorAll('.time-slot-btn');
    let selectedSlot = '';

    timeSlotButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Reset all button styles
            timeSlotButtons.forEach(btn => btn.classList.remove('selected'));

            // Highlight the selected button
            this.classList.add('selected');
            selectedSlot = this.value;

            // Handle the selection of time slot
            document.getElementById('delivery_timeSlot').setAttribute('data-selected-slot', selectedSlot);
            
            // You can add additional logic here, for example:
            // - Update hidden input for form submission
            // - Show confirmation to the user
            console.log("Selected Time Slot: " + selectedSlot);
        });
    });

    document.getElementById('delivery_date').addEventListener('change', function() {
      const timeSlotDiv = document.getElementById('delivery_timeSlot');
      if (this.value) {
          timeSlotDiv.style.display = 'block';
      } else {
          timeSlotDiv.style.display = 'none';
      }
    });

// Capture selected time slot
    document.querySelectorAll('.time-slot-btn').forEach(button => {
        button.addEventListener('click', function() {
            document.getElementById('delivery_timeSlot').setAttribute('data-selected-slot', this.value);
            alert('You selected: ' + this.value);
        });
    });