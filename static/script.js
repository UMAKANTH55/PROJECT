function addStudent() {
    // Get form values
    var name = document.getElementById('name').value;
    var rollNo = document.getElementById('roll_no').value;
    var course = document.getElementById('course').value;


     // Clear form fields
     document.getElementById('name').value = '';
     document.getElementById('roll_no').value = '';
     document.getElementById('course').value = '';

    if (name && rollNo && course) {
    var studentData = {
        name: name,
        roll_no: rollNo,
        course: course
    };

    // Make fetch request to Flask API endpoint
    fetch('/student/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(studentData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
    }
    function updateStudent() {
        var id = document.getElementById('student_id').value; 
        var name = document.getElementById('update_name').value;
        var rollNo = document.getElementById('update_roll_no').value;
        var course = document.getElementById('update_course').value;
    
        // Clear form fields
        document.getElementById('student_id').value = '';
        document.getElementById('update_name').value = '';
        document.getElementById('update_roll_no').value = '';
        document.getElementById('update_course').value = '';
    
        if (name && rollNo && course) {
            var updatedStudentData = {
                name: name,
                roll_no: rollNo,
                course: course
            };
    
            fetch('/student/' + id, {  
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(updatedStudentData),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Update Success:', data);
            })
            .catch((error) => {
                console.error('Update Error:', error);
            });
        }
    }
    function deleteStudent() {
        var id = document.getElementById('delete_student_id').value; 
        document.getElementById('delete_student_id').value = '';
        if (id) {
            fetch('/student/' + id, {  
                method: 'DELETE',
            })
            .then(response => response.json())
            .then(data => {
                console.log('Delete Success:', data);
            })
            .catch((error) => {
                console.error('Delete Error:', error);
            });
        }
    }
    // Function to check student info
function checkStudentInfo() {
    var id = document.getElementById('student_id_check').value;
    document.getElementById('student_id_check').value = '';
    if (id) {
        fetch('/student/' + id, { 
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
    
            // Check if the expected properties are present in the server response
            if (data && data.name && data.roll_no && data.course) {
                var name = data.name;
                var roll_no = data.roll_no;
                var course = data.course;
    
                // Create HTML content with the retrieved student information
                var htmlContent = `
                    <h3>Student Information</h3>
                    <p><strong>Name:</strong> ${name}</p>
                    <p><strong>Roll Number:</strong> ${roll_no}</p>
                    <p><strong>Course:</strong> ${course}</p>
                `;
    
                // Update the content of the container
                document.getElementById('studentInfoContainer').innerHTML = htmlContent;

            } else {
                console.error('Invalid or missing data in the server response.');
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
    
}
