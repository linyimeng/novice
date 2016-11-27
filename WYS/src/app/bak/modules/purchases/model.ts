export class Gdav {
    constructor(
        public batch,
        public productiondate,
        public validity,
        public remark
    ){}
}

export class OrderDetail {
    constructor(
        public order:string,
        public goods:number,
        public quantity:number,
        public price:number,
        public gdav:string,
        public gsav:string
    ){}
}



export class Order {
    constructor(
        public ordercode:string,
        public totalquantity:number,
        public totalprice:number,
        public company:number,
        public type:number,
        public remark:string,
        public creator:number
    ){}
}