import { Component,OnInit,Input,Output,EventEmitter } from '@angular/core';
import { Router } from '@angular/router';

import { DepartmentService } from '../wysservices/department.service';

@Component({
   selector: 'departmentSelect',
   template: `
        <select [(ngModel)]="pk" (change)="onChange($event.target.value)">
            <option value="">无所属部门{{dpk}}</option>
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
        this._departmentService.list().subscribe(
            departments=>{
                this.departments=departments;
                /** 解决刚加载时因为异步加载机制而导致的部门名称无法显示，解决方法，延迟等待 */
                setTimeout(()=>{
                    if(typeof(this.dpk)=="object") {
                        this.pk="";
                    } else {
                        this.pk=this.dpk;
                    }
                    console.log(this.pk);
                },80);
            },
            error=>alert(error)
        );
        
    }

    onChange(pk) {
        this.departpk.emit(pk);
    }
}

