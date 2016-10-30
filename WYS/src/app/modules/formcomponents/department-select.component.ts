import { Component,OnInit,Input,Output,EventEmitter } from '@angular/core';
import { Router } from '@angular/router';

import { DepartmentService } from '../wysservices/department.service';

@Component({
   selector: 'departmentSelect',
   template: `
        <select [(ngModel)]="pk" (change)="onChange($event.target.value)">
            <option value="">无上级部门{{dpk}}</option>
            <option [value]="depart.pk" *ngFor="let depart of departments">{{depart.name}}</option>
        </select>
   `,
   providers:[ DepartmentService ],
})
export class DepartmentSelectComponent implements OnInit{
    
    @Output() departpk = new EventEmitter<string>();
    pk:string = null;
    @Input() dpk:any;

    departments:any;

    constructor(
        private _departmentService:DepartmentService
    ) { }

    ngOnInit() {
        this._departmentService.get_department_list().subscribe(
            departments=>{
                this.departments=departments;
            },
            error=>alert(error),
            ()=>this.pk=this.dpk
        );
    }
    onChange(pk) {
        this.departpk.emit(pk);
    }
}

