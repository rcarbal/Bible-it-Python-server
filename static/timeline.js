let COLOMNS;

function setupHistoricalPeriods(historicalPeriods, biblicaPeriods, figures){
    COLOMNS = new ColumnChecker(-4004, 2019);
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

        addBiblicalFiguresToTimeline(name, birth, death, period);
    }
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
    let row;

    if (periodType == "history"){
        type = "hist-";
        paddingType = "hist-pad";
        row = "";
    } else if(periodType == "bible-figures"){
        type = 'bible-';
        paddingType = 'bible-pad';
        row = "-row"
    } else {
        type = 'bible-';
        paddingType = 'bible-pad';
        row = "";
    }

    // find the years element
    let firstYearElement = document.getElementById(`${type}${firstYear}${row}`);
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
    let row;

    if (period == 'biblical'){
        type = 'bible-';
        row = '-row';
    }

    // Get the year column information
    let firstYearColumn = COLOMNS.years[`${birth}`];

    // find the first year row that will hold all the columns
    let firstYearRow = document.getElementById(`${type}${birth}${row}`);
    let columnToUse;
    
    // add the number of necessary columns.
    for (let i = firstYearColumn; i < firstYearColumn + 1; i++){
        
        let birthColumn = document.createElement("div");
        birthColumn.classList.add("col-1");
        firstYearRow.appendChild(birthColumn);
        columnToUse = birthColumn;
        COLOMNS.addAYearColumn(birth);
    }

    // fingd the last year last year of timeline
    let lastYearElement = document.getElementById(`${type}${death}${row}`);
    let figureEnd = document.createElement("div");
    figureEnd.textContent = `${name}'s death`;
    figureEnd.classList.add("col-1");
    figureEnd.classList.add("p-0");
    figureEnd.classList.add("ml-1");
    figureEnd.classList.add('sec');
    figureEnd.classList.add('sec-stop');
    lastYearElement.appendChild(figureEnd);

    // Add an epty column under death column
    console.log("add empty");
    let emptyColumn = document.createElement("div");
    emptyColumn.classList.add("col-1");
    console.log("Added death clip");
    emptyColumn.classList.add("death-clip");
    emptyColumn.classList.add("ml-1");
    let nextRowAfterDeathRow = document.getElementById(`${type}${death + 1}${row}`);
    nextRowAfterDeathRow.appendChild(emptyColumn);

    // Now that you have the columns to use add the properties
    columnToUse.classList.add("p-0");
    columnToUse.classList.add("sec");
    columnToUse.classList.add("sec-start");
    columnToUse.classList.add("ml-1");
    columnToUse.textContent = name;

    //loop through all the current biblical figures years
    let yearToStartLoop = birth + 1;

    for(i = yearToStartLoop; i < death; i++){
        console.log("test loop");
        
        if (i == 0){
            initialYear++;
            continue;
        }
        // Get the year columns within a years row
        let rowOfLoop = document.getElementById(`${type}${i}${row}`);

        // need to add a column
        let lifeSpanColumn = document.createElement("div");
        lifeSpanColumn.classList.add("col-1");
        lifeSpanColumn.classList.add("sec");
        lifeSpanColumn.classList.add("height-bible");
        lifeSpanColumn.classList.add("ml-1");
        rowOfLoop.appendChild(lifeSpanColumn);
    }
}