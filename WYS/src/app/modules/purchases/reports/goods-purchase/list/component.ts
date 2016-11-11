import { Component,OnInit } from '@angular/core';

import { OrderService } from '../../../../wysservices/order.service';

@Component({   
   selector: 'goods-purchase-reports',
   templateUrl: 'list.html',
   providers:[OrderService]
})
export class GoodsPurchaseListComponent implements OnInit{

    ordergoodss:any;

    constructor(
        private _orderService:OrderService
    ){}

    ngOnInit(){
        this._orderService.get_ordergoods_list('i').subscribe(
            ordergoodss=>{
                this.ordergoodss = ordergoodss;
            },
            error=>alert(error)
        )
    }

}
