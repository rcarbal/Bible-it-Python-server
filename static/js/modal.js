$('#reusableModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  data = $(event.relatedTarget.dataset)[0];
  var modal = $(this);

  // setup word difinition information
  if (data.modaltype == "1") {
    setupWordModal(modal, data)
  }
  else {
    console.log(data)
    setupChapterModal(data, modal)
  }
})

function setupChapterModal(dataRef, modal){
       let section = dataRef.section
       let book = dataRef.book
       let bookId = dataRef.book_id
       let chapter = dataRef.chapter
       let chapterId = dataRef.chapter_id
       let verse = dataRef.verse

       modal.find('.modal-title').text(`${book}: Chapter: ${chapter}`)

       // get the modal
       let element = document.getElementsByClassName("modal-body")[0];
       element.innerHTML = "";
       // create the list
       let ol = document.createElement('ol');
       element.appendChild(ol)

       getChapter(bookId, chapterId, verse, ol);
}

function setupWordModal(modal, dataReference) {
  let word = dataReference.word
  modal.find('.modal-title').text(dataReference.word + " Information")

  // SETUP the POS
  var pos_list = dataReference.pos;

  // change pos 
  var pos;
  if (pos_list == 'PROPN') {
    pos = 'NOUN';
  } else {
    pos = pos_list;
  }
  element = document.getElementsByClassName("modal-body")[0];
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
}

// Retrieves Definitions
function getDefinitions(word, defintionOderedList, pos) {
  axios.get("/api/word/definition?word=" + word)
      .then((response) => {

          // get modal div
          const arr = response.data;
          let posValue = POS[pos];

          let addedToDom = 0;

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
                              addedToDom++
                          });
                      };
                  }else {
                    console.log()
                  }

                  // end of posMached if statement
              }
              // end of dataDefinition if statement

              if (addedToDom == 0){
                let liItem = document.createElement('li');
                liItem.innerHTML = "No definitions retrieved";
                defintionOderedList.appendChild(liItem);
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

  const intToMatch = parseInt(verse);
    axios.get(`/api/chapter?book=${bookId}&chapter=${chapter}&verse=${verse}`)
        .then((response)=>{

            // loop through all the verses and add them tho the ordered list
            const verses = response['data']

            var count = 1;

            for (verse in verses){
                const verseString = verses[verse];

                let li = document.createElement('li');

                // find the verse we need
                if (intToMatch == count){
                  // var strongEl = document.createElement("strong");
                  // strongEl.innerHTML = verseString;
                  li.innerHTML = `<strong><u>${verseString}</u></strong>`;
                  li.classList.add("pt-2");
                  li.classList.add("pb-2");
                }else {
                  li.innerHTML = verseString;
                }
                ol.appendChild(li);
                count++;
            }

        });
}
