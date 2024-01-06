// script.js

function openFileBrowser() {
    document.getElementById('fileInput').click();
    document.getElementById('fileInput').addEventListener('change', function() {
        // Analyze selected file
        handleFileSelection();
    });
}


function handleFileSelection() {
    var selectedFile = document.getElementById('fileInput').files[0];
    var selectedFileDisplay = document.getElementById('selectedFile');
    
    var uploadButton = document.getElementById('uploadButton');

    if (selectedFile) {
        var allowedExtensions = ['wav'];
        var fileExtension = selectedFile.name.slice((selectedFile.name.lastIndexOf(".") - 1 >>> 0) + 2);
        if (allowedExtensions.includes(fileExtension.toLowerCase())) {
            document.getElementById('uploadForm').submit();
            selectedFileDisplay.innerHTML = '<img src="https://cdn-icons-png.flaticon.com/512/181/181603.png" alt="Audio Icon" id="audioIcon"> Selected file: ' + selectedFile.name;

            uploadButton.style.display = 'none';
        } else {
            var errorDisplay = document.getElementById('error');
            errorDisplay.innerHTML = 'Error: Please select a wav audio file.';

            uploadButton.style.display = 'block';
        }
    }
}

function evaluateSong(file_path) {
    var evaluateButton = document.getElementById('evaluateButton');
    var newUploadButton = document.getElementById('newUploadButton');
    var loadingSpinner = document.getElementById('loadingSpinner');
    var selectedFileDisplay = document.getElementById('selectedFile');
    var genre;

    newUploadButton.style.display = 'none';
    evaluateButton.style.display = 'none';
    loadingSpinner.style.display = 'block';
    selectedFileDisplay.style.display = 'none';

    // Make an asynchronous request to the server for file processing
    fetch('/process_file', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ file_path: file_path })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response from server:', data);
        genre = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    setTimeout(function() {
        // Redirect to /result after evaluation
        loadingSpinner.style.display = 'none';

        // Navigate to the new URL
        window.location.href = 'result/' + genre;

    }, 4500); // Simulated 4.5 seconds evaluation time
}

function goToHomePage() {
    window.location.href = '/';
}