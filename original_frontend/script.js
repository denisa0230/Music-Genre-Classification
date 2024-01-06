// script.js

function openFileBrowser() {
    document.getElementById('fileInput').click();
}

function handleFileSelection() {
    var selectedFile = document.getElementById('fileInput').files[0];
    var selectedFileDisplay = document.getElementById('selectedFile');
    var errorDisplay = document.getElementById('error');
    var uploadButton = document.getElementById('uploadButton');
    var evaluateButton = document.getElementById('evaluateButton');
    var loadingSpinner = document.getElementById('loadingSpinner');

    if (selectedFile) {
        var allowedExtensions = ['mp3', 'wav', 'ogg', 'pdf'];
        var fileExtension = selectedFile.name.slice((selectedFile.name.lastIndexOf(".") - 1 >>> 0) + 2);

        if (allowedExtensions.includes(fileExtension.toLowerCase())) {
            selectedFileDisplay.innerHTML = '<img src="https://cdn-icons-png.flaticon.com/512/181/181603.png" alt="Audio Icon" id="audioIcon"> Selected file: ' + selectedFile.name;
            errorDisplay.innerHTML = '';

            uploadButton.style.display = 'none';
            evaluateButton.style.display = 'block';
        } else {
            selectedFileDisplay.innerHTML = '';
            errorDisplay.innerHTML = 'Error: Please select a valid audio file (mp3, wav, ogg).';

            uploadButton.style.display = 'block';
            evaluateButton.style.display = 'none';
            loadingSpinner.style.display = 'none';
        }
    } else {
        selectedFileDisplay.innerHTML = '';
        errorDisplay.innerHTML = 'No file selected.';

        uploadButton.style.display = 'block';
        evaluateButton.style.display = 'none';
        loadingSpinner.style.display = 'none';
    }
}

function evaluateSong() {
    var evaluateButton = document.getElementById('evaluateButton');
    var loadingSpinner = document.getElementById('loadingSpinner');

    evaluateButton.style.display = 'none';
    loadingSpinner.style.display = 'block';

    setTimeout(function() {
        // Redirect to result.html after evaluation
        window.location.href = 'result.html';
    }, 3000); // Simulated 3 seconds evaluation time
}
