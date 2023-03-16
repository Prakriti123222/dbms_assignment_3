function updateDisciplines() {
  var program = document.getElementById("current_program").value;
  var discipline = document.getElementById("major_discipline");
  discipline.innerHTML = "";

  if (program === "BTECH") {
    var options = [
      { value: "mechanical", label: "Mechanical Engineering" },
      { value: "electrical", label: "Electrical Engineering" },
      { value: "computer", label: "Computer Science and Engineering" },
      { value: "chemical", label: "Chemical Engineering"},
      { value: "civil", label: "Civil Engineering"},
      { value: "materials", label: "Material Science and Engineering"},
    ];
  } else if (program === "MTECH") {
    var options = [
      { value: "mechanical", label: "Mechanical Engineering" },
      { value: "electrical", label: "Electrical Engineering" },
      { value: "computer", label: "Computer Science and Engineering" },
      { value: "chemical", label: "Chemical Engineering"},
      { value: "civil", label: "Civil Engineering"},
      { value: "materials", label: "Material Science and Engineering"},
    ];
  } else if (program === "MSC"){
      var options = [
      { value: "physics", label: "Physics" },
      { value: "chemistry", label: "Chemistry" },
      { value: "maths", label: "Maths" },
      ];

  }
   else {
    var options = [];
  }

  options.forEach(function (option) {
    var element = document.createElement("option");
    element.value = option.value;
    element.innerHTML = option.label;
    discipline.appendChild(element);
  });
}




var current_program= [  { id: "mechanical", label: "Mechanical Engineering", value: "mechanical" },  { id: "electrical", label: "Electrical Engineering", value: "electrical" },  { id: "computer", label: "Computer Engineering", value: "computer" }];

var container = document.createElement("div");
container.id = "major_discipline";

var label = document.createElement("label");
label.innerHTML = "major_discipline";
container.appendChild(label);
container.appendChild(document.createElement("br"));

current_program.forEach(function (branch) {
  var input = document.createElement("input");
  input.type = "checkbox";
  input.id = branch.id;
  input.name = "major_discipline[]";
  input.value = branch.value;

  var label = document.createElement("label");
  label.innerHTML = branch.label;
  label.setAttribute("for", branch.id);

  container.appendChild(input);
  container.appendChild(label);
  container.appendChild(document.createElement("br"));
});

document.body.appendChild(container);
