import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   moduleId: module.id,
   selector: 'supplier-right',
   templateUrl: 'supplier-right.component.html'
})
export class SupplierRightComponent {
    constructor(
        private router:Router
    ) {}

    show_supplier_create() {
        this.router.navigate(['/purchases/supplier/create']);
    }
}

