import { Component,OnInit } from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';

import { CompanyService } from '../../../wysservices/company.service';

import { Supplier } from '../model';

@Component({
   
   selector: 'supplier-detail',
   templateUrl: 'detail.html'
})
export class SupplierDetailComponent implements OnInit{
    supplier:Supplier = new Supplier(null,null,true,null,null,null,null,null,null);

    constructor(
        private _supplierService:CompanyService,
        private router:Router,
        private activatedRoute:ActivatedRoute
    ){}

    ngOnInit(){
        this.activatedRoute.params.forEach(
            params=>{
                let pk = +params['pk'];
                this._supplierService.get_company_detail(pk).subscribe(
                    supplier=>this.supplier=supplier,
                    error=>alert(error)
                );
            }
        );
    }

    save_goods(){
        let json = JSON.stringify(this.supplier);
        let pk = this.supplier.pk;
        this._supplierService.put_update_company(pk,json).subscribe(
            supplier=>{
                console.log(Supplier);
                this.router.navigate(['purchases/supplier/list']);
            },
            error=>alert(error)
        );
    }
}
