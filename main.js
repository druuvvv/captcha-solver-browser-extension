function extensionCode(){


    async function imageToCanvas(imgElement) {
        var tries = 0;
        const retryDelay = 100;
        while(tries < 5){
            try{
            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');

            // Set the canvas size to match the image size
            canvas.width = imgElement.width;
            canvas.height = imgElement.height;

            // Draw the image onto the canvas
            context.drawImage(imgElement, 0, 0, imgElement.width, imgElement.height);

        // Get the image data
            const imageData = context.getImageData(0, 0, imgElement.width, imgElement.height);
            const dataArray = Array.from(imageData.data); // Convert ImageData to array
            console.log(dataArray);
            return {dataArray , "width" : imgElement.width , "height" : imgElement.height};
        }
        catch(err){
            console.error("failed to fetch image data");
            tries++;
            await new Promise(resolve => setTimeout(resolve, retryDelay));
        }
    }
    }
    function findInputTag(element){
        let parentTag = element.parentNode; // find parent node of the captcha image
        let possibleInputTag = [];
        
        // recursively keep going up the DOM tree untill an input tag is found
        // this input tag will be closest to the captcha image as it belongs to its closest parent Node
        while(possibleInputTag.length == 0){
            possibleInputTag = parentTag.getElementsByTagName("input");
            parentTag = parentTag.parentNode;   
        }
        return possibleInputTag[0];
    }
    
    async function apiCall(binaryData){
        const response  = await fetch(`http://localhost:5000/`,{
            method : "POST",
            headers : {
              'Content-Type' : 'application/json',
            },
            body: JSON.stringify(
              binaryData
             )})
             
        const captchaCode = await response.json();
        console.log(captchaCode);
        return captchaCode;
    }
    
    function updateInputBox(captchaCode , elt){
        const inputTag = findInputTag(elt);
        inputTag.value = captchaCode;

        // Stop the mutation observer until the URL changes
        observer.disconnect();
    }
    
    // async function convertToBase64(imgURL ,element){
    //     fetch(imgURL)
    //     .then(response => response.blob())
    //     .then(blob => {
    //         // Create a FileReader to read the blob as Data URL
    //         var reader = new FileReader();
    
    //         reader.onload = function () {
    //             // Get the Base64 representation of the image
    //             var base64String = reader.result;
    
    //             apiCall(base64String)
    //             .then(response => updateInputBox(response , element))
                
    //         };
    
    //         // Read the blob as a Data URL
    //         reader.readAsDataURL(blob);
    //     })
    //     .catch(error => console.error('Error fetching the image:', error));
    
    // }
    
    const img = document.getElementsByTagName("img");
    
    //Trying to find captcha image by searching captcha word in id and classname
    for(elt of img){
        var className = elt.className.toLowerCase();
        var idName = elt.id.toLowerCase();
        var srcUrlLowercased = elt.src.toLowerCase();
        var altInfo = elt.alt.toLowerCase();
    
        if(className.includes("captcha") || idName.includes("captcha") || altInfo.includes("captcha")){
            observer.disconnect();
            console.log(elt)
            imageToCanvas(elt)
            .then(binaryData => apiCall(binaryData)) // apiCall to convert the image to captcha code
            .then(response => updateInputBox(response , elt)) // update the input box with the captcha code
            break;
        }
        
    }
    
    
}

var observer = new MutationObserver(extensionCode);
// Configure the observer to watch for changes in the entire subtree of the document
var observerConfig = { subtree: true, childList: true };
// Start observing the document
observer.observe(document.documentElement, observerConfig);
// Initial run when the page is loaded
extensionCode();