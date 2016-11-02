import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { CompanyService } from '../../../wysservices/company.service';

import { Supplier } from '../model';
@Component({
   
   selector: 'supplier-create',
   templateUrl: 'create.html'
})
export class SupplierCreateComponent{
    supplier:Supplier = new Supplier(null,null,true,null,null,null,null,null,null);

    constructor(
        private _supplierService:CompanyService,
        private router:Router
    ){}

    save_goods(){
        this.supplier.is_vendor = true;
        let json = JSON.stringify(this.supplier);
        this._supplierService.post_create_company(json).subscribe(
            supplier=>{
                console.log(Supplier);
                this.router.navigate(['purchases/supplier/list']);
            },
            error=>alert(error)
        );
    }
}
