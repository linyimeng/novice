export class StaticAttr{
    constructor(
        approvalnumber:string,
        origin:string,
    ) {}
}
export class Goods{
    constructor(
        pk:number,
        type:number,
        name:string,
        specification:string,
        unit:string,
        barcode:string,
        manufacturer:string,
        costprice:number,
        salesprice:number,
        remark:string,
        static_attr:string,
    ){}
}