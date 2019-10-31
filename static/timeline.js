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
    console.log(name);
    let type;
    let row;

    if (period == 'biblical'){
        type = 'bible-';
        row = '-row';
    }


    if (name === "Joseph"){
        console.log("Found Joseph");
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
        COLOMNS.addChildToBiblicalRow(birth, birthColumn);
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
    COLOMNS.addChildToBiblicalRow(death, figureEnd);

    // Add div that will contain the death and trans clip divs
    let emptyColumn = document.createElement("div");
    emptyColumn.classList.add("col-1");
    emptyColumn.classList.add("clip-death");
    emptyColumn.classList.add("ml-1");

    // setup the correct year for transition between -1 ans 1
    let forDeathColumn;
    if (death + 1 < 0 || death + 1 > 0){
        forDeathColumn = death + 1;
    } else {
        forDeathColumn = 1
    }

    let nextRowAfterDeathRow = document.getElementById(`${type}${forDeathColumn}${row}`);
    nextRowAfterDeathRow.appendChild(emptyColumn);
    COLOMNS.addChildToBiblicalRow(death + 1, emptyColumn);

    // Now that you have the columns to use add the properties
    columnToUse.classList.add("p-0");
    columnToUse.classList.add("sec");
    columnToUse.classList.add("sec-start");
    columnToUse.classList.add("ml-1");
    columnToUse.textContent = name;

    //loop through all the current biblical figures years
    let yearToStartLoop = birth + 1;

    for(i = yearToStartLoop; i < death; i++){
        
        if (i == 0){
            // initialYear++;
            continue;
        }
        // Get the year columns within a years row
        let rowOfLoop = document.getElementById(`${type}${i}${row}`);

        // get the last the last child column
        const child = COLOMNS.getYear(i);
        let lastChild;
        let isDeathColumn;
        let isTransClip;

        if (child.length > 0){
            lastChild = child.pop();
        }

        // check if last child is death column
        if (lastChild != undefined){
            
            // check if it is a deathclip
            if (lastChild.classList.contains("clip-death")){
                isDeathColumn = lastChild.classList.contains("clip-death");
            } else if (lastChild.classList.contains("clip-trans")){
                isTransClip = lastChild.classList.contains("clip-trans");
            }
        }

        // if first column is death-clip
        if(isDeathColumn){
            let transColumn = document.createElement("div");
            transColumn.classList.add("col-1");
            transColumn.classList.add("clip-trans")
            rowOfLoop.appendChild(transColumn);
            COLOMNS.addChildToBiblicalRow(i, transColumn);
        }else if(isTransClip){
            let deathColumn = document.createElement("div");
            deathColumn.classList.add("col-1");
            deathColumn.classList.add("clip-death")
            rowOfLoop.appendChild(deathColumn);
            COLOMNS.addChildToBiblicalRow(i, deathColumn);
        }else{
            // need to add a column
            let lifeSpanColumn = document.createElement("div");
            lifeSpanColumn.classList.add("col-1");
            lifeSpanColumn.classList.add("sec");
            lifeSpanColumn.classList.add("height-bible");
            lifeSpanColumn.classList.add("ml-1");
            rowOfLoop.appendChild(lifeSpanColumn);
            COLOMNS.addChildToBiblicalRow(i, lifeSpanColumn);
        }
    }
}