import { Component,OnInit } from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';

import { StaffService } from '../../../wysservices/staff.service';

export class Staff{
    constructor(
        public pk:number,
        email:string,

        name:string,
        work_address:string,
        office_phone:string,
        office_address:string,
        office_landline:string,
        cardid:string,
        bank_account:string,
        sex:string,
        marital_status:string,
        birthday:string,
        entry_time:string,
        isarchive:boolean,
        remark:string,

        public job:number,
        public department:number,
    ){}
}

@Component({
   selector: 'staff-detail',
   templateUrl: 'detail.html',
   providers:[StaffService]
})
export class StaffDetailComponent implements OnInit{
    staff:Staff = new Staff(null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);
    staff_pk:any;
    dpk:any;
    constructor(
        private _staffservice:StaffService,
		private router:Router,
        private activatedroute:ActivatedRoute
    ){}

    ngOnInit() {
        this.activatedroute.params.forEach(
            params=>{
                let pk= +params['pk'];
                this.staff_pk = pk;
                this._staffservice.retrieve(pk).subscribe(
                    staff=>{
                        this.staff=staff;
                        this.dpk = staff.department;
                    },
                    error=>alert(error)
                );
            }
        );
    }

    save_staff() {
        let json = JSON.stringify(this.staff);
        let pk = this.staff.pk;
        this._staffservice.update(pk,json).subscribe(
            staff=>this.router.navigate(['/personnel/staff/list']),
            error=>alert(error),
        )
    }

    setdepartmentPk(pk) {
        this.staff.department = pk;
        this.dpk = pk;
    }

    setjobspk(jpk) {
        this.staff.job = jpk;
    }

}

