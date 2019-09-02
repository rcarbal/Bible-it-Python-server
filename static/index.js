let element = null;

$(document).on('show.bs.modal', '.fade', function (e) {

    var modal = $(this).data('modal');
    var word;

    if (modal == 2) {

        // sets up the inexact word list
        word = $(this).data('word2');
    } else {

        // sets up the exact word list
        word = $(this).data('word');
    }


    var pos_list = $(this).data('pos');
    var pos = pos_list

    element = this.getElementsByClassName("modal-body")[0];
    element.innerHTML = "";

    // create the definition header
    let definitionHeader = document.createElement('h6');
    definitionHeader.innerHTML = "-" + pos + " " + word;

     // create the definition h6 element
     let headerEl = document.createElement('h6');
     headerEl.innerHTML = "- Definitions"

    // create <hr> tag
    let hrTag = document.createElement('hr');


    // create the synonym header
    let synonymHeader = document.createElement('h6');
    synonymHeader.innerHTML = "- Synonyms"

    // create ordered list
    let ol = document.createElement('ol');

    element.appendChild(definitionHeader);
    element.appendChild(headerEl);
    element.appendChild(ol);
    element.appendChild(hrTag);
    element.appendChild(synonymHeader);

    // callback
    const callback = (synonymOrderedList) => {
        element.appendChild(synonymOrderedList)

    }


    // Call definitions urk
    getDefinitions(word,ol, pos)




});


// Retrieves Definitions
function getDefinitions(word, defintionOderedList, pos) {
    axios.get("/api/word/definition?word=" + word)
        .then((response) => {

            console.log("Getting Definitions");

            // get modal div
            const arr = response.data;

                arr.forEach((definition) => {

                    let fl = definition.fl;

                    if (fl.toLowerCase() == pos.toLowerCase()){
                        // loop through the shortdefs
                        let shortdef = definition.shortdef;

                        shortdef.forEach((singelDef) => {
                            // append single definition to the module                        
                            let liItem = document.createElement('li');
                            liItem.innerHTML = singelDef;
                            defintionOderedList.appendChild(liItem);
                        });
                    };
                });
            getSynonyms(word);
        });
}
// Retrieves Synonnyms
function getSynonyms(word) {
    axios.get("/api/word/synonym?word=" + word)
        .then((response) => {

            // data is an array, loop through the array
            data = response.data;

            for(i in data){

                // deep nested json, retrieve synonym array
                let def = data[i]['def'][0]['sseq'];
                 
                // sseq property has multiple elements
                for(x in def){

                    let synonyms = def[x][0][1]['syn_list'];
                    // loop through the synonyms
                    for (y in synonyms){
                        
                        synonyms[y].forEach((root)=>{

                            // append root to module
                            let span = document.createElement("SPAN");
                            span.innerHTML =', ';
                            let anchor = document.createElement('a');
                            anchor.setAttribute('href', '#');
                            anchor.text = root['wd'];

                            // span.appendChildan(anchor);
                            element.appendChild(anchor);
                            element.appendChild(span);

                        });
                    }
                    
                }
            }
        });
}



