function setupHistoricalPeriods(historicalPeriods, biblicaPeriods, figures){
    // place historical periods
    addHistoricalPeriods(historicalPeriods);

    // place the correct biblical periods in the timeline
    addBiblicalPeriods(biblicaPeriods);
    
    // place the biblical figures in the timeline
    const correctFigures = JSON.parse(figures.replace(/&#34;/g,'"'));

    for (c in correctFigures){
        const name = correctFigures[c]['name'];
        const birth = correctFigures[c]['birth'];
        const death = correctFigures[c]['death'];
        const period = 'biblical';

        //addBiblicalFiguresToTimeline(name, birth, death, period);
    }

    //let columnChecker = new ColumnChecker(-4004, -4002);
}

function addHistoricalPeriods(historicalPeriods){
    // remove escape characters
    const correctHistoricalPeriods = JSON.parse(historicalPeriods.replace(/&#34;/g,'"'));
        // place the correct historical period on the timeline.
     for (h in correctHistoricalPeriods){
         // loop through all the years
         let firstYear = correctHistoricalPeriods[h]['first_year'];
         let lastYear = correctHistoricalPeriods[h]['last_year'] - 1;
         let period = correctHistoricalPeriods[h]['name'];
         let periodType = "history";
         addClassesToYear(firstYear, lastYear, period, periodType);
     }
 }

 function addBiblicalPeriods(biblicaPeriods){
    const correctBiblicalPeriods = JSON.parse(biblicaPeriods.replace(/&#34;/g,'"'));

    for (b in correctBiblicalPeriods){
            const firstYear = correctBiblicalPeriods[b]['first_year'];
            const lastYear =  correctBiblicalPeriods[b]['last_year'] - 1;
            const name = correctBiblicalPeriods[b]['name']; 
            const period = 'biblical'
            addClassesToYear(firstYear, lastYear, name, period);
    }
}

function addClassesToYear(firstYear, lastYear, period, periodType){
    let type;
    let paddingType;

    if (periodType == "history"){
        type = "hist-";
        paddingType = "hist-pad";
    } else {
        type = 'bible-';
        paddingType = 'bible-pad';
    }

    // find the years element
    let firstYearElement = document.getElementById(`${type}${firstYear}`);
    let eraTitle = document.createElement("div");
    eraTitle.textContent = period;
    let firstChild = firstYearElement.firstChild;

    if (firstChild == null){
        firstYearElement.appendChild(eraTitle);
    } else {
        firstYearElement.insertBefore(eraTitle, firstChild);
    }

    let lastYearElement = document.getElementById(`${type}${lastYear}`);

    // add classes to element
    firstYearElement.classList.add("sec-start");
    lastYearElement.classList.add("sec-stop");

    // loop through all years and add classes
    let initialYear = firstYear;

   
    for(i = firstYear; i < lastYear + 1; i++){
        // console.log(initialYear);
        // console.log(i);

        if (i == 0){
            initialYear++;
            continue;
        }

        // find the years between
        let yearElement = document.getElementById(`${type}${initialYear}`);
        yearElement.classList.add('sec');
        yearElement.classList.add(paddingType);

        initialYear++;
    }
    let emptyElement = document.createElement('div');
    emptyElement.textContent = 'PERIOD';
}

function addBiblicalFiguresToTimeline(name, birth, death, period){
    let type;

    if (period == 'biblical'){
        type = 'bible-'
    }

    // find the first year
    let firstYearElement = document.getElementById(`${type}${birth}`);
    // add a row to the first year

    let firstrow = document.createElement("div");
    firstrow.classList.add("row");
    firstYearElement.appendChild(firstrow);

    // add the birth column
    let birthColumn = document.createElement("div");
    birthColumn.classList.add("col-1");
    birthColumn.classList.add("p-0");
    birthColumn.classList.add("sec");
    birthColumn.classList.add("sec-start");
    birthColumn.textContent = name;
    firstrow.appendChild(birthColumn);


    // let figureStart = document.createElement("div");
    // figureStart.textContent = name;
    // figureStart.classList.add("sec");
    // figureStart.classList.add("sec-start");
    // figureStart.classList.add("bible-fig");
    // firstYearElement.appendChild(figureStart);

    // // fing the second last year
    // let lastYearElement = document.getElementById(`${type}${death}`);
    // let figureEnd = document.createElement("div");
    // figureEnd.textContent = `${name}'s death`;
    // figureEnd.classList.add('sec');
    // figureEnd.classList.add('sec-stop');
    // figureEnd.classList.add('bible-fig');
    // lastYearElement.appendChild(figureEnd);

    // loop through to complete timeline's lifespan

    let initialYear = birth;

    for(i = birth; i < death; i++){
        
        if (i == 0){
            initialYear++;
            continue;
        }

        // // find the years between
        // let yearElement = document.getElementById(`${type}${initialYear}`);
        // let row = document.createElement("div");
        // row.classList.add("row");
        // row.classList.add("height-bible");
        // row.id = `${type}${initialYear}-row`;
        // yearElement.appendChild(row);

        // // add figure column
        // let column = document.createElement("div");
        // column.classList.add("col-1");
        // column.classList.add("sec");
        // row.appendChild(column);


        initialYear++;
    }
}