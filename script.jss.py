const text = [

    "Frontend Developer",

    "Web Designer",

    "Tech Enthusiast"
];

let word = 0;

let char = 0;

const typing =
document.getElementById("typing");

function type(){

    if(char < text[word].length){

        typing.textContent +=
        text[word].charAt(char);

        char++;

        setTimeout(type,100);
    }

    else{

        setTimeout(erase,1500);
    }
}

function erase(){

    if(char > 0){

        typing.textContent =
        text[word].substring(0,char-1);

        char--;

        setTimeout(erase,50);
    }

    else{

        word++;

        if(word >= text.length){

            word = 0;
        }

        setTimeout(type,300);
    }
}

type();