import { Component,Input,OnInit } from '@angular/core';
import { OrderService } from '../../../wysservices/order.service';
import { OrderDetail,Order } from '../../model';
@Component({
   selector: 'purchaseorders-create',
   templateUrl: 'create.html',
   providers:[OrderService]
})
export class PurchaseOrdersCreateComponent implements OnInit{
    datetime:string;
    order:Order = new Order(null,null,null,null,null,null,null,null);
    detail:OrderDetail[];
    constructor(
        private _orderService:OrderService
    ){}

    ngOnInit(){
        this.order.ordercode = this._orderService.get_ordercode();
        this.datetime = new Date().toLocaleString();
    }

    save_order() {
        this.order.detail = JSON.stringify(this.detail);
        let json = JSON.stringify(this.order);
        console.log(json);
    }

    setsupplierPk(pk) {
        this.order.company = Number(pk);
    }
}
