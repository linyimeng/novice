import { Component,OnInit } from '@angular/core';
import { OrderService } from '../../../wysservices/order.service';

@Component({
   selector: 'goods-sales-reports',
   templateUrl: 'goods-sales-reports.html',
   providers:[OrderService]
})
export class GoodsSalesReportsComponent implements OnInit{
    ordergoodss:any;
    constructor(
        private _orderService:OrderService
    ){}

    ngOnInit(){
        this._orderService.get_ordergoods_list('o').subscribe(
            ordergoodss=>{
                this.ordergoodss=ordergoodss;
            },
            error=>alert(error)
        )
    }
}
