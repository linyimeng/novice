import { Component,OnInit } from '@angular/core';

import { OrderService } from '../../../../wysservices/order.service';

@Component({   
   selector: 'goods-purchase-reports',
   templateUrl: 'list.html',
   providers:[OrderService]
})
export class GoodsPurchaseListComponent implements OnInit{

    ordergoodss:any;
    filtered_data:any;

    totalquantity:number;
    totalprice:number

    constructor(
        private _orderService:OrderService
    ){}

    ngOnInit(){
        this._orderService.get_ordergoods_list('i').subscribe(
            ordergoodss=>{
                this.ordergoodss = ordergoodss;
                this.filtered_data = ordergoodss;
                this.set_total();
            },
            error=>alert(error)
        )
    }

    set_total(){
        let totalquantity = 0;
        let totalprice = 0;
        for(let og of this.filtered_data){
            totalquantity = totalquantity + Number(og.quantity);
            totalprice = totalprice + (Number(og.price * Number(og.quantity)));
        }
        this.totalprice = totalprice;
        this.totalquantity = totalquantity;
    }

    setsupplierPk(pk) {
        this.filtered_data = this.ordergoodss.filter(item=>item.company==pk);
    }

    filter_goodsname(value) {
        this.filtered_data = this.ordergoodss.filter(item=>
            item.gsav.name.indexOf(value)!=-1);
        this.set_total();
    }

    filter_date(startdate,enddate){
        if(startdate=='') startdate='2008-08-08';
        if(enddate=='') enddate='2088-06-06';
        if(!this.check_date(startdate) || !this.check_date(enddate)) return;
        let start = new Date(startdate);
        let end = new Date(enddate);
        this.filtered_data = this.ordergoodss.filter(og=>{
            let joined = new Date(og.joined.substr(0,10));
            if(joined >= start && joined <= end) {
                console.log(og.joined.substr(0,10));
                return true;
            } else {
                return false;
            }
        });
        this.set_total();
    }

    check_date(date) {
        var result = date.match(/((^((1[8-9]\d{2})|([2-9]\d{3}))(-)(10|12|0?[13578])(-)(3[01]|[12][0-9]|0?[1-9])$)|(^((1[8-9]\d{2})|([2-9]\d{3}))(-)(11|0?[469])(-)(30|[12][0-9]|0?[1-9])$)|(^((1[8-9]\d{2})|([2-9]\d{3}))(-)(0?2)(-)(2[0-8]|1[0-9]|0?[1-9])$)|(^([2468][048]00)(-)(0?2)(-)(29)$)|(^([3579][26]00)(-)(0?2)(-)(29)$)|(^([1][89][0][48])(-)(0?2)(-)(29)$)|(^([2-9][0-9][0][48])(-)(0?2)(-)(29)$)|(^([1][89][2468][048])(-)(0?2)(-)(29)$)|(^([2-9][0-9][2468][048])(-)(0?2)(-)(29)$)|(^([1][89][13579][26])(-)(0?2)(-)(29)$)|(^([2-9][0-9][13579][26])(-)(0?2)(-)(29)$))/);
        if(result==null) {
            return false;
        }
        return true;
    }
    

}
