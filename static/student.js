// Define a function to update the major discipline options based on the selected program
function updateMajorDisciplines() {
    // Get the selected program from the program dropdown
    var selectedProgram = document.getElementById("current_program").value;
    // Get the major discipline options container element
    var majorDisciplinesContainer = document.getElementById("major-disciplines");
    // Clear the existing major discipline options
    majorDisciplinesContainer.innerHTML = "";
    // Add the major discipline options based on the selected program
    if (selectedProgram === "BTECH") {
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="mechanical"> Mechanical Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="electrical"> Electrical Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="computer"> Computer Science and Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="chemical"> Chemical Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="civil"> Civil Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="materials"> Materials Science and Engineering</label><br>';
    } else if (selectedProgram === "MTECH") {
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="mechanical"> Mechanical Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="electrical"> Electrical Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="computer"> Computer Science and Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="chemical"> Chemical Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="civil"> Civil Engineering</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="materials"> Materials Science and Engineering</label><br>';
    } else if (selectedProgram === "MSC") {
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="physics"> Physics</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="chemistry"> Chemistry</label><br>';
        majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="maths"> Mathematics</label><br>';
    }
  }
  
  function updateMinorDisciplines() {
      // Get the selected program from the program dropdown
      var selectedProgram = document.getElementById("minor_discipline").value;
      console.log(selectedProgram);
      // Get the major discipline options container element
      var a = document.getElementById("minor-disciplines");
      // Clear the existing major discipline options
      if(a.innerHTML.length > 0){
          a.innerHTML="";
      } else {
          a.innerHTML="";
          a.innerHTML += '<label><input type="checkbox" name="minor" value="mechanical"> Mechanical Engineering</label><br>';
          a.innerHTML += '<label><input type="checkbox" name="minor" value="electrical"> Electrical Engineering</label><br>';
          a.innerHTML += '<label><input type="checkbox" name="minor" value="computer"> Computer Science and Engineering</label><br>';
          a.innerHTML += '<label><input type="checkbox" name="minor" value="chemical"> Chemical Engineering</label><br>';
          a.innerHTML += '<label><input type="checkbox" name="minor" value="civil"> Civil Engineering</label><br>';
          a.innerHTML += '<label><input type="checkbox" name="minor" value="materials"> Materials Science and Engineering</label><br>';
      }
  
      // Add the major discipline options based on the selected program
      
      // } else if (selectedProgram === "MTECH") {
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="mechanical"> Mechanical Engineering</label><br>';
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="electrical"> Electrical Engineering</label><br>';
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="computer"> Computer Science and Engineering</label><br>';
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="chemical"> Chemical Engineering</label><br>';
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="civil"> Civil Engineering</label><br>';
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="materials"> Materials Science and Engineering</label><br>';
      // } else if (selectedProgram === "MSC") {
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="physics"> Physics</label><br>';
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="chemistry"> Chemistry</label><br>';
      //     majorDisciplinesContainer.innerHTML += '<label><input type="checkbox" name="major" value="maths"> Mathematics</label><br>';
      // }
  }