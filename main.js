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

async function apiCall(base64String){
    const response  = await fetch("http://localhost:5000/",{
        method : "POST",
        headers : {
          'Content-Type' : 'application/json',
        },
        body: JSON.stringify({
          base64 : `${base64String}`,
         
        })})
    const captchaCode = await response.json();

    return captchaCode;
}

function updateInputBox(captchaCode , elt){
    const inputTag = findInputTag(elt);
    inputTag.value = captchaCode;
}

async function convertToBase64(imgURL ,element){
    fetch(imgURL)
    .then(response => response.blob())
    .then(blob => {
        // Create a FileReader to read the blob as Data URL
        var reader = new FileReader();

        reader.onload = function () {
            // Get the Base64 representation of the image
            var base64String = reader.result;

            apiCall(base64String)
            .then(response => updateInputBox(response , element))
            
        };

        // Read the blob as a Data URL
        reader.readAsDataURL(blob);
    })
    .catch(error => console.error('Error fetching the image:', error));

}

const img = document.getElementsByTagName("img");

//Trying to find captcha image by searching captcha word in id and classname
for(elt of img){
    var className = elt.className.toLowerCase();
    var idName = elt.id.toLowerCase();
    var srcUrlLowercased = elt.src.toLowerCase();
    var altInfo = elt.alt.toLowerCase();

    if(className.includes("captcha") || idName.includes("captcha") || altInfo.includes("captcha")){
        //check if URL in base64    
        if(srcUrlLowercased.includes("data:image")){
            apiCall(elt.src) // apiCall to convert the image to captcha code
            .then(response => updateInputBox(response , elt))
        }
        else{
            convertToBase64(elt.src , elt) // convert the image url to base64string and then doing the same api call
        }
        break;
    }
    
}

