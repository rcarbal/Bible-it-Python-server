class FigureColors {
    constructor(){
        this.currentIndex = 0;
        this.colors = ['#3318CC', '#675F99','#3884F', '#FFC478', '#CC6418'];
    }

    getColor(){
        if (this.currentIndex === 4){
            const color = this.colors[this.currentIndex];
            this.currentIndex = 0;
            return color;
        }
        const color = this.colors[this.currentIndex];
        this.currentIndex++;
        return color;
    }
}