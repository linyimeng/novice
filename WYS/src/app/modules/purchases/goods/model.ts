export class StaticAttr{
    constructor(
        approvalnumber:string,
        origin:string,
    ) {}
}
export class Goods{
    constructor(
        public pk:number,
        public type:number,
        name:string,
        specification:string,
        unit:string,
        barcode:string,
        manufacturer:string,
        costprice:number,
        salesprice:number,
        remark:string,
        public static_attr:string,
    ){}
}