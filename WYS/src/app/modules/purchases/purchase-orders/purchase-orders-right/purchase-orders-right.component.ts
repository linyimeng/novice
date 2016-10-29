import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   
   selector: 'purchase-orders-right',
   templateUrl: 'purchase-orders-right.component.html'
})
export class PurchaseOrdersRightComponent {
    constructor(
        private router:Router
    ) {}

    show_goods_create() {
        this.router.navigate(['/purchases/purchase-orders/create']);
    }
}

