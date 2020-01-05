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
        
    });
  });

$(document).on('show.bs.modal', '.fade', function (e) {

    var modal = $(this).data('modal');
    var word;

    if (modal == 1 || modal == 2) {

        const index = $(this).data('index');

        if (modal == 2) {

            // sets up the inexact word list
            word = $(this).data('word2');
        } else {

            // sets up the exact word list
            word = $(this).data('word');
        }

        // Gets the POS
        var pos_list = $(this).data('pos');

        // Officiial
        var pos;
        if(pos_list == 'PROPN'){
            pos = 'NOUN';
        }else{
            pos = pos_list;
        }

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
        synonymHeader.innerHTML = "- Synonyms Found in the bible NIV"

        // create ordered list
        let ol = document.createElement('ol');

        element.appendChild(definitionHeader);
        element.appendChild(headerEl);
        element.appendChild(ol);
        element.appendChild(hrTag);
        element.appendChild(synonymHeader);

        // Call definitions urk
        getDefinitions(word, ol, pos)
    } else {
        let section = $(this).data('section');
        let book = $(this).data('book');
        let bookId = $(this).data('book_id');
        let chapter = $(this).data('chapter');
        let verse = $(this).data('verse');

        // get the modal
        element = this.getElementsByClassName("modal-body")[0];
        element.innerHTML = "";
        // create the list
        let ol = document.createElement('ol');
        element.appendChild(ol)

        getChapter(bookId, chapter, verse, ol);
    }

});


// Retrieves Definitions
function getDefinitions(word, defintionOderedList, pos) {
    axios.get("/api/word/definition?word=" + word)
        .then((response) => {

            // get modal div
            const arr = response.data;
            let posValue = POS[pos];

            arr.forEach((dataDefinition) => {

                // this contains full lowercase string expression
                // such as 'adverb', use this to find the POS value 
                if (dataDefinition.hasOwnProperty('fl')) {
                    let fl = dataDefinition.fl.toLowerCase();
                    let pattern = new RegExp("(^|\\W)" + posValue + "($|\\W)");
                    let posMatched = fl.match(pattern);

                    if (posMatched) {

                        // if (fl.includes(value.toLowerCase())){
                        if (fl.toLowerCase().match()) {
                            // loop through the shortdefs
                            let shortdef = dataDefinition.shortdef;

                            shortdef.forEach((singelDef) => {
                                // append single definition to the module                        
                                let liItem = document.createElement('li');
                                liItem.innerHTML = singelDef;
                                defintionOderedList.appendChild(liItem);
                            });
                        };
                    }
                }

            });
            getSynonyms(word, posValue);
        });
}
// Retrieves Synonnyms
function getSynonyms(word, pos) {
    axios.get("/api/word/synonym?word=" + word)
        .then((response) => {

            let complete_bible = "";

            // data is an array, loop through the array
            data = response.data;

            for (i in data) {

                const synData = data[i];
                if (synData.hasOwnProperty('bible_string')) {
                    rawBibleJSON = synData['bible_string'];
                    complete_bible = JSON.stringify(rawBibleJSON);
                    continue;
                }

                // deep nested json, retrieve synonym array
                const whatIsDef = data[i];

                let synonyms;

                if (typeof whatIsDef === 'string') {

                    for (let i = 1; i <= data.length; i++) {
                        const synData = data[i];

                        // check that synonym is the bible
                        let patternSyn = new RegExp("(^|\\W)" + synData + "($|\\W)");
                        let synMatched = complete_bible.match(patternSyn);

                        if (synMatched) {
                            // Add synonym to DOM
                            let span = document.createElement("SPAN");
                            span.innerHTML = ', ';
                            let anchor = document.createElement('a');
                            anchor.text = synData;
                            anchor.setAttribute('href',
                                `/word_search?word=${synData}`);


                            element.appendChild(anchor);
                            element.appendChild(span);

                        }
                    }

                    break;

                } else {
                    let def = data[i]['def'][0]['sseq'];
                    let dataPos = data[i]['fl'];
                    let pattern = new RegExp("(^|\\W)" + pos + "($|\\W)");
                    let posMatched = dataPos.match(pattern);
                    if (!posMatched) {
                        continue;
                    }

                    // sseq property has multiple elements
                    for (x in def) {

                        synonyms = def[x][0][1]['syn_list'];
                        // loop through the synonyms
                        for (y in synonyms) {

                            synonyms[y].forEach((root) => {

                                // append root to module
                                let span = document.createElement("SPAN");
                                span.innerHTML = ', ';
                                let anchor = document.createElement('a');
                                anchor.text = root['wd'];
                                anchor.setAttribute('href',
                                    `/word_search?word=${root['wd']}`);



                                let patternSyn = new RegExp("(^|\\W)" + root['wd'] + "($|\\W)");
                                let synMatched = complete_bible.match(patternSyn);

                                if (synMatched) {
                                    element.appendChild(anchor);
                                    element.appendChild(span);
                                }

                            });
                        }

                    }
                }
            }
        });
}

function getChapter(bookId, chapter, verse, ol){
    axios.get(`/api/chapter?book=${bookId}&chapter=${chapter}&verse=${verse}`)
        .then((response)=>{            

            // loop through all the verses and add them tho the ordered list
            const verses = response['data']

            for (verse in verses){
                const verseString = verses[verse];

                let li = document.createElement('li');
                li.innerHTML = verseString;
                ol.appendChild(li);
            }

        });
}

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

                response.data.forEach((data)=>{
                    console.log(data);
                    // check for high match score
                    if (data[1] >= 85){
                        let div = document.createElement("div");
                        div.innerHTML = data[0];

                        previewDiv.appendChild(div);
                    }
                });

                // set visibility of search preview div to visible            
                previewDiv.style.visibility = "visible";

                EVENT_LISTENER_RUNNING = false;
            });
        }
        else if (inputValue.length == 0){
            previewDiv.style.visibility = "hidden";

            EVENT_LISTENER_RUNNING = false;
        }
    }

}