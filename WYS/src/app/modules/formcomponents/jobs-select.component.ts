import { Component,OnInit,Input,Output,EventEmitter,OnChanges } from '@angular/core';
import { Router } from '@angular/router';

import { DepartmentService } from '../wysservices/department.service';

@Component({
   selector: 'jobsSelect',
   template: `
        <select [(ngModel)]="pk" (change)="onChange($event.target.value)">
            <option value="">无职位</option>
            <option [value]="job.pk" *ngFor="let job of jobs">{{job.name}}</option>
        </select>
   `,
   providers:[ DepartmentService ],
})
export class JobsSelectComponent {
    
    @Output() jobspk = new EventEmitter<string>();
    pk:string = null;
    _dpk:any;
    @Input() 
    set dpk(dpk:any) {
        if(typeof(dpk)=="undefined") {
            this._dpk = "";
        } else {
            this._dpk = dpk;
            this.get_djobs();
        }
    }
    @Input() jpk:any;

    jobs:any;


    constructor(
        private _departmentService:DepartmentService
    ) { }

    get_djobs(){
        this._departmentService.get_department_jobs(this._dpk).subscribe(
            jobs=>{
                this.jobs=jobs;
                /** 解决刚加载时因为异步加载机制而导致的部门名称无法显示，解决方法，延迟等待 */
                setTimeout(()=>{
                    if(typeof(this.jpk)=="object") {
                        this.pk="";
                    } else {
                        this.pk=this.jpk;
                    }
                    console.log(this.pk);
                },60);
            },
            error=>alert(error)
        );
    }

    onChange(pk) {
        this.jobspk.emit(pk);
    }
}

