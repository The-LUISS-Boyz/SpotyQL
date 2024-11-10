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
        // Expand the box content
        content.style.height = content.scrollHeight + 'px';
        content.style.padding = '15px'; // Adding padding when expanded
        icon.textContent = '▲';

        // Calculate the position to scroll to the center of the box
        const boxRect = boxes[index].getBoundingClientRect();
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const targetPosition = scrollTop + boxRect.top - (window.innerHeight / 2) + (boxRect.height / 2);

        // Smoothly scroll to the calculated position
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    } else {
        // Collapse the box content
        content.style.height = '0px';
        content.style.padding = '0';
        icon.textContent = '▼';
    }
}

  function addResultBox(button, query) {
    const resultBoxContainer = button.parentNode.querySelector('.result-box-container');

    // Check if a result box already exists
    if (resultBoxContainer.querySelector('.result-box')) {
        console.log("Result box already exists.");
        return;
    }

    // Create a new div element for the result box
    const resultBox = document.createElement('div');
    resultBox.classList.add('result-box');

    // Add content with the existing close button design
    resultBox.innerHTML = `
        <span class="close-btn" onclick="closeResultBox(this)">X</span>
        <pre><code>Executing...</code></pre>
    `;

    // Await query execution
    window.pywebview.api.execute_query(query).then(
        result => resultBox.innerHTML = result
    )

    
    // Append the result box to the container
    resultBoxContainer.appendChild(resultBox);
    console.log("Result box added.");

    // Smooth scroll within the `.box-content` container
    const boxContent = button.closest('.box-content');
    boxContent.scrollTo({
        top: boxContent.scrollHeight,
        behavior: 'smooth'
    });
}

function addConsoleResultBox(button, textBox) {
  const resultBoxContainer = document.querySelector('.console-result-box-container');

  // Clear any existing result to avoid multiple boxes
  resultBoxContainer.innerHTML = '';

  // Get the query text from the textBox input
  const query = textBox.value;

  // Create a new div element for the result box
  const resultBox = document.createElement('div');
  resultBox.classList.add('console-result-box');

  // Add a close button and placeholder text while query executes
  resultBox.innerHTML = `
      <span class="console-close-btn" onclick="closeConsoleResultBox(this)">X</span>
      <pre><code>Executing...</code></pre>
  `;

  // Await execution of query using the query text
  window.pywebview.api.execute_query_str(query).then(result => {
      // Update the result box with the returned result
      resultBox.innerHTML = `
          <span class="console-close-btn" onclick="closeConsoleResultBox(this)">X</span>
          <pre><code>${result}</code></pre>
      `;
  });

  // Append the result box to the container
  resultBoxContainer.appendChild(resultBox);
  console.log("Console result box added.");
}

function closeConsoleResultBox(closeButton) {
  closeButton.parentNode.remove();
  console.log("Console result box removed.");
}

function handleEnter(event) {
    // Check if the Enter key (keyCode 13) was pressed
    if (event.key === "Enter") {
        // Call addConsoleResultBox, passing the text box as an argument
        const textBox = event.target;
        const button = document.querySelector('.console-search-button');
        addConsoleResultBox(button, textBox);
    }
}

function closeResultBox(closeButton) {
    const resultBox = closeButton.parentNode;
    const boxContent = resultBox.closest('.box-content');

    // Remove the result box
    resultBox.remove();
    console.log("Result box removed.");

    // Scroll back to the top of `.box-content`
    boxContent.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function openIndexPage() {
  window.location.href = 'index.html';
}

function toggleMenu() {
    const menu = document.querySelector('.nav-menu');
    const hamburgerIcon = document.querySelector('.hamburger');

    menu.classList.toggle('show'); // Toggle visibility

    // Switch between hamburger and X icons
    if (menu.classList.contains('show')) {
        hamburgerIcon.textContent = '✖'; // Change to "X"
    } else {
        hamburgerIcon.textContent = '☰'; // Change back to hamburger
    }
}