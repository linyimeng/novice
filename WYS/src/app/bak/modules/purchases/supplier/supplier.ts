import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   
   selector: 'supplier',
   templateUrl: 'supplier.html'
})
export class SupplierComponent {
    constructor(
        private router:Router
    ) {}

    show_supplier_create() {
        this.router.navigate(['/purchases/supplier/create']);
    }
}

