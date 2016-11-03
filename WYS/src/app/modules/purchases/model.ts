export class OrderDetail {
    constructor(
        public order:string,
        public goods:number,
        public quantity:number,
        public price:number,
        public dynamic_attr:string,
        public remark:string
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
        public creator:number,
        public detail:string
    ){}
}