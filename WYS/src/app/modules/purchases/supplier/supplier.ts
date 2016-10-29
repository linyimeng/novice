export class Supplier {
    constructor(
        public pk:number,
        name:string,
        public is_vendor:boolean,
        landline:string,
        phone:string,
        email:string,
        fax:string,
        address:string,
        remark:string
    ){}
}