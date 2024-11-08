/* function closeWelcome() {
    document.getElementById("welcomeMessage").style.display = "none";
  } */


    //STORE the closedWelcome in the session
    function closeWelcome() {
      document.getElementById("welcomeMessage").style.display = "none";
      sessionStorage.setItem("welcomeClosed", "true");
    }

    window.onload = function() {
      if (sessionStorage.getItem("welcomeClosed") === "true") {
        document.getElementById("welcomeMessage").style.display = "none";
      }
    };


// JavaScript to handle the toggle action on each box
function toggleBox(index) {
    const boxes = document.querySelectorAll('.expandable-box');
    const content = boxes[index].querySelector('.box-content');
    const icon = boxes[index].querySelector('.vish-icon');
  
    // If the box is already expanded, collapse it
    if (content.style.height === '0px' || content.style.height === '') {
      // Get the scrollHeight (the full height of the content)
      content.style.height = content.scrollHeight + 'px';
      content.style.padding = '15px'; // Adding padding when expanded
  
      // Change the icon to an up arrow
      icon.textContent = '▲';
    } else {
      // Collapse the box by setting height to 0
      content.style.height = '0px';
      content.style.padding = '0'; // Remove padding when collapsed
  
      // Change the icon back to a down arrow
      icon.textContent = '▼';
    }
  }