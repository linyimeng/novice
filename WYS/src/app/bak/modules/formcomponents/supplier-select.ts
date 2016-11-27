import { Component,OnInit,Input,Output,EventEmitter } from '@angular/core';
import { Router } from '@angular/router';

import { CompanyService } from '../wysservices/company.service';
@Component({
   selector: 'supplierSelect',
   template: `
        <select [(ngModel)]="pk" (change)="onChange($event.target.value)">
            <option [value]="supplier.pk" *ngFor="let supplier of suppliers">{{supplier.name}}</option>
        </select>
   `,
   providers:[ CompanyService ],
})
export class SupplierSelectComponent implements OnInit{
    
    @Output() supplierpk = new EventEmitter<string>();
    pk:string = null;
    @Input() spk:any;

    suppliers:any;

    constructor(
        private _supplierService:CompanyService
    ) { }

    ngOnInit() {
        this._supplierService.get_supplier_list().subscribe(
            suppliers=>{
                this.suppliers=suppliers;
                /** 解决刚加载时因为异步加载机制而导致的部门名称无法显示，解决方法，延迟等待 */
                setTimeout(()=>{
                    if(typeof(this.spk)=="object") {
                        this.pk="";
                    } else {
                        this.pk=this.spk;
                    }
                    console.log(this.pk);
                },80);
            },
            error=>alert(error)
        );
        
    }

    onChange(pk) {
        this.supplierpk.emit(pk);
    }
}