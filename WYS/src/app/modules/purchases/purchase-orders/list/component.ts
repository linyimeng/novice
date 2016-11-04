import { Component,OnInit  } from '@angular/core';
import { OrderService } from '../../../wysservices/order.service';
@Component({
   
   selector: 'purchase-orders-list',
   templateUrl: 'list.html',
   providers:[OrderService]
})
export class PurchaseOrdersListComponent implements OnInit{
    iorders:any;

    constructor(
        private _orderService:OrderService
    ){}

    ngOnInit(){
        this._orderService.get_list_io('i').subscribe(
            iorders=>this.iorders=iorders,
            error=>alert(error)
        );
    }

}

