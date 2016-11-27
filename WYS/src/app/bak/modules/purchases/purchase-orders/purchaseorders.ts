import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   selector: 'purchaseorders',
   templateUrl: 'purchaseorder.html'
})
export class PurchaseOrdersComponent {
    constructor(
        private router:Router
    ) {}

    show_goods_create() {
        this.router.navigate(['/purchases/purchase-orders/create']);
    }
}

