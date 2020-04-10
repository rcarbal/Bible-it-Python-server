// 9:10am
let element = null;

const POS = {
    "INTJ": "interjection", "NOUN": "noun", "ADP": "adposition",
    "VERB": "verb", "NUM": "numeral",
    "PUNCT": "punctuation", "PART": "particle", "X": "other",
    "PRON": "pronoun", "ADJ": "adjective", "CCONJ": "coordinating conjunction",
    "ADV": "adverb", "SPACE": "whitespace", "AUX": "auxiliary",
    "DET": "determiner", "PROPN": "proper noun", "SYM": "symbol"
}

let EVENT_LISTENER_RUNNING = false;

// get child from preview div
$(document).ready(function() {
    $('#previewDiv').on('click', function(event) {
        // event.stopPropagation();
        const question = event.target.innerHTML;

        // get search and set search bar
        const search = document.getElementById('searchInput');
        search.value = question;

        // call server to get response
        if (question.split(" ").length){
            document.getElementById("searchForm").submit();
        }
    });
  });

function echoWord(){
    
    if (!EVENT_LISTENER_RUNNING){

        EVENT_LISTENER_RUNNING = true;
        
        let input = document.getElementById('searchInput');
        let previewDiv = document.getElementById('previewDiv');

        // remove all previewDiv's children if any
        if (previewDiv.hasChildNodes()){
            previewDiv.innerHTML = "";
        }

        let inputValue = input.value;

        if (inputValue.length > 0){
            axios.get(`/api/question_match?input=${inputValue}`)
            .then((response)=>{

            let count = 0;

                response.data.forEach((data)=>{
                    // check for high match score
                    if (data[1] >= 85){
                        let div = document.createElement("div");
                        div.innerHTML = data[0];
                        div.classList.add("text-left");
                        div.classList.add("pt-1");
                        div.classList.add("pl-3");

                        previewDiv.appendChild(div);
                        count++;
                    }
                });

                if (count > 0){

                let inputShouldNotHave = input.classList.contains("clear_bottom");
                if(!inputShouldNotHave){
                    // add clear-bottom
                    input.classList.add("clear_bottom");
                }

                // set visibility of search preview div to visible
                let previewShouldNotHave = previewDiv.classList.contains("show_pre");
                if(!previewShouldNotHave){
                    previewDiv.classList.add("show_pre");
                }
                    previewDiv.style.visibility = "visible";
                }

                EVENT_LISTENER_RUNNING = false;
            });
        }
        else if (inputValue.length == 0){
            // remove class because preview is hidden
            let inputShouldHave = input.classList.contains("clear_bottom");
            if(inputShouldHave){
                // add clear-bottom
                input.classList.remove("clear_bottom");
            }

            let previewShouldHave = previewDiv.classList.contains("show_pre");
            if(previewShouldHave){
                previewDiv.classList.remove("show_pre");
            }

            previewDiv.style.visibility = "hidden";

            EVENT_LISTENER_RUNNING = false;
        }
    }

}

//calls the endpoint to retrieve response by from backend.
function getQuestion(question){
    // axios.get(`/word_search?question=${question}`);   
    axios.get(`/word_search?question=${question}`);
}
