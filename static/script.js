document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('file-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('File uploaded successfully:', data);
    })
    .catch(error => {
        console.error('Error uploading file:', error);
    });
});

document.getElementById('play').addEventListener('click', function() {
    fetch('/play', { method: 'POST' });
});

document.getElementById('pause').addEventListener('click', function() {
    fetch('/pause', { method: 'POST' });
});

document.getElementById('rewind').addEventListener('click', function() {
    fetch('/rewind', { method: 'POST' });
});

document.getElementById('forward').addEventListener('click', function() {
    fetch('/forward', { method: 'POST' });
});