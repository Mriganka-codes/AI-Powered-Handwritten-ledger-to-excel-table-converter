document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.getElementById('imageInput');
    const convertBtn = document.getElementById('convertBtn');
    const loader = document.getElementById('loader');
    const downloadLink = document.getElementById('downloadLink');
    const selectedFileDisplay = document.getElementById('selectedFile');
    const uploadArea = document.getElementById('uploadArea');
    const hamburger = document.getElementById('hamburger');
    const nav = document.getElementById('nav');
        if (hamburger && nav) {
            hamburger.addEventListener('click', function() {
                nav.classList.toggle('nav--active');
            });
    }


    function handleFile(file) {
        if (file && file.type.startsWith('image/')) {
            selectedFileDisplay.textContent = `Selected: ${file.name}`;
            selectedFileDisplay.style.display = 'block';
            convertBtn.disabled = false;
        } else {
            selectedFileDisplay.style.display = 'none';
            convertBtn.disabled = true;
            if (file) {
                alert('Please select a valid image file (e.g., JPG, PNG).');
            }
        }
    }

    // Handle file selection via button
    imageInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        handleFile(file);
    });

    // Handle drag and drop
    uploadArea.addEventListener('dragover', function(e) {
        e.preventDefault();
        uploadArea.classList.add('drag-over');
    });

    uploadArea.addEventListener('dragleave', function(e) {
        e.preventDefault();
        uploadArea.classList.remove('drag-over');
    });

    uploadArea.addEventListener('drop', function(e) {
        e.preventDefault();
        uploadArea.classList.remove('drag-over');
        const file = e.dataTransfer.files[0];
        // Assign dropped file to the input
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        imageInput.files = dataTransfer.files;
        
        handleFile(file);
    });

    // Handle convert button click
    convertBtn.addEventListener('click', async function() {
        const file = imageInput.files[0];
        if (!file) {
            alert('Please select an image file first.');
            return;
        }

        loader.style.display = 'block';
        downloadLink.style.display = 'none';
        convertBtn.disabled = true;

        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await fetch('/api/convert', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                downloadLink.href = url;
                downloadLink.download = 'output.xlsx';
                downloadLink.style.display = 'block';
            } else {
                const errorData = await response.json();
                alert(`Error: ${errorData.error}`);
            }
        } catch (error) {
            console.error('Conversion Error:', error);
            alert(`An unexpected error occurred: ${error.message}`);
        } finally {
            loader.style.display = 'none';
            convertBtn.disabled = false;
        }
    });
});
