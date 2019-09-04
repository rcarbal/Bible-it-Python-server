let element = null;

const POS = {
    "INTJ": "interjection", "NOUN": "noun", "ADP": "adposition",
    "VERB": "verb", "NUM": "numeral",
    "PUNCT": "punctuation", "PART": "particle", "X": "other",
    "PRON": "pronoun", "ADJ": "adjective", "CCONJ": "coordinating conjunction",
    "ADV": "adverb", "SPACE": "whitespace", "AUX": "auxiliary",
    "DET": "determiner", "PROPN": "proper noun", "SYM": "symbol"
}

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
    synonymHeader.innerHTML = "- Synonyms Found in the bible NIV"

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
    getDefinitions(word, ol, pos)




});


// Retrieves Definitions
function getDefinitions(word, defintionOderedList, pos) {
    axios.get("/api/word/definition?word=" + word)
        .then((response) => {

            console.log("Getting Definitions");

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
                        console.log(synData);

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


