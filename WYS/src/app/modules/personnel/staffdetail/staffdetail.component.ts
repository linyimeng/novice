import { Component,OnInit } from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';

import { StaffService } from '../../wysservices/staff.service';

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

        job:number,
        department:number,
    ){}
}

@Component({
   selector: 'staff-detail',
   templateUrl: 'staffdetail.component.html',
   providers:[StaffService]
})
export class StaffdetailComponent implements OnInit{
    staff:Staff = new Staff(null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);
    staff_pk:any;
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
                this._staffservice.get_emp_detail(pk).subscribe(
                    staff=>this.staff=staff,
                    error=>alert(error)
                );
            }
        );
    }

    save_staff() {
        let json = JSON.stringify(this.staff);
        let pk = this.staff.pk;
        this._staffservice.put_update_emp(pk,json).subscribe(
            staff=> {
                    console.log(JSON.stringify(staff));
					this.router.navigate(['/personnel/staff/list']);
                 },
            error=>{alert(error)},
        )
    }

}

