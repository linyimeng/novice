import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { StaffService } from '../../wysservices/staff.service';

export class Staff{
    constructor(
        email:string,
        loginname:string,
        password:string,

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
   selector: 'staff-creat',
   templateUrl: 'staffcreat.component.html',
   providers:[StaffService]
})
export class StaffcreatComponent{
    staff:Staff = new Staff(null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null);
    constructor(
		private _staffservice:StaffService,
		private router:Router
	) { }

    /** 保存员工 */
    save_staff(){
        let json = JSON.stringify(this.staff);
        console.log(json);
        this._staffservice.post_create_emp(json).subscribe(
            staff=>{
                console.log(JSON.stringify(staff));
				this.router.navigate(['/personnel/staff/list']);
            },
            error=>alert(error)
        )
    }
}
