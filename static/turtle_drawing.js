// Heavily inspired by MrToph's L-System
// import * as d3path from 'd3-path';

class TurtleDrawing {
  constructor (angleIncrement, stepSize) {
    this.startAngle = 90;
    this.turnAngle = this.startAngle;
    this.angleIncrement = parseInt(angleIncrement);
    this.stepSize = stepSize;
    this.currentX = 0;
    this.currentY = 0;
    this.annotations = [];
  }

  renderString (s) {
    let strokeLength = this.stepSize;

    let path = d3.path();

    path.moveTo(this.currentX, this.currentY);

    for (let i = 0; i < s.length; i++) {
      if (s[i].match("[A-Z]")) {
        this.currentX = this.nextXPoint(this.currentX);
        this.currentY = this.nextYPoint(this.currentY);

        path.lineTo(this.currentX, this.currentY);

      } else if (s[i].match("[a-z]")) {
        this.currentX = this.nextXPoint(this.currentX);
        this.currentY = this.nextYPoint(this.currentY);

        path.moveTo(this.currentX, this.currentY);
      } else {
        switch (s[i]) {
          // case 'f': {
          //   this.currentX = this.nextXPoint(this.currentX);
          //   this.currentY = this.nextYPoint(this.currentY);

          //   path.moveTo(this.currentX, this.currentY);
          //   break;
          // }
          case '+': {
            this.moveAngle('+');
            break;
          }
          case '-': {
            this.moveAngle('-');
            break;
          }
        }
      }
    }

    return path;

  }

  makeAnnotation(i) {
    var a = {
      "cx": this.currentX,
      "cy": this.currentY,
      "r": 2,
      "text": i,
      "textWidth": 150,
      "textOffset": [35, 40] 
    };

    this.annotations.push(a);
  }

  nextXPoint (x) {
    return x - (this.stepSize * Math.cos(this.turnAngle * (Math.PI / 180)));
  }

  nextYPoint (y) {
    return y - (this.stepSize * Math.sin(this.turnAngle * (Math.PI / 180)));
  }

  moveAngle (direction) {
    switch (direction) {
      case '+': {
        this.turnAngle -= this.angleIncrement;
        break;
      }

      case '-': {
        this.turnAngle += this.angleIncrement;
        break;
      }
    }
  }

}
