import { Component,Input,OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { OrderService } from '../../../wysservices/order.service';

import { Order } from '../../model';
@Component({
   selector: 'purchaseorders-detail',
   templateUrl: 'detail.html',
   providers:[OrderService]
})
export class PurchaseOrdersDetailComponent implements OnInit{
    orderdetail:Order = new Order(null,null,null,null,null,null,null);
    constructor(
        private _orderService:OrderService,
        private activatedroute:ActivatedRoute
    ){}

    ngOnInit(){
        this.activatedroute.params.forEach(
            params=>{
                let ordercode = params['ordercode'];
                this._orderService.get_order_detail(ordercode).subscribe(
                    orderdetail=>{
                        this.orderdetail = orderdetail;
                        console.log(this.orderdetail);
                    },
                    error=>alert(error)
                );
            }
        );
    }
}
