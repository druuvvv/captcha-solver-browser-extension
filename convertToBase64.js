export function convertToBase64(imgURL){
    fetch(imgURL)
    .then(response => response.blob())
    .then(blob => {
        // Create a FileReader to read the blob as Data URL
        var reader = new FileReader();

        reader.onload = function () {
            // Get the Base64 representation of the image
            var base64String = reader.result;

            // Log or use the Base64 string as needed
            console.log(base64String);
        };

        // Read the blob as a Data URL
        reader.readAsDataURL(blob);
    })
    .catch(error => console.error('Error fetching the image:', error));

}

