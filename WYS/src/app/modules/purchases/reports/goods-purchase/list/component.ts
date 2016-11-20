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

    constructor(
        private _orderService:OrderService
    ){}

    ngOnInit(){
        this._orderService.get_ordergoods_list('i').subscribe(
            ordergoodss=>{
                this.ordergoodss = ordergoodss;
                this.filtered_data = ordergoodss;
            },
            error=>alert(error)
        )
    }

    setsupplierPk(pk) {
        this.filtered_data = this.ordergoodss.filter(item=>item.company==pk);
    }

    filter_goodsname(value) {
        this.filtered_data = this.ordergoodss.filter(item=>
            item.gsav.name.indexOf(value)!=-1);
    }

    

}
