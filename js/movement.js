export class Movement {
    constructor({position,limits}) {
        this.position = position ?? {x: 0, y: 0, z: 0};
        this.limits = limits ?? {x: 0, y: 0};
    }
    updatePosition(deltaPosition,priority) {}
}