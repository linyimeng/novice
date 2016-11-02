import { Component,OnInit} from '@angular/core';

import { CompanyService } from '../../../wysservices/company.service';

@Component({
   
   selector: 'supplier-list',
   templateUrl: 'list.html'
})

export class SupplierListComponent implements OnInit{
    suppliers:any;

    constructor(
        private _supplierService:CompanyService
    ){}

    ngOnInit(){
        this._supplierService.get_supplier_list().subscribe(
            suppliers=>this.suppliers=suppliers,
            error=>alert(error)
        );
    }
}

