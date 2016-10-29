import { Component,OnInit} from '@angular/core';
import { Router } from '@angular/router';

import { StaffService } from '../../wysservices/staff.service';

@Component({
   moduleId: module.id,
   selector: 'staff-content',
   templateUrl: 'staffcontent.component.html',
   providers:[StaffService]
})
export class StaffcontentComponent implements OnInit{
    staffs:any;

	constructor(
		private staffservice:StaffService,
		private router:Router
	) { }

	ngOnInit() {
		this.get_emp_list();
	}

	get_emp_list() {
		return this.staffservice.get_emp_list()
							    .subscribe(
									 staffs=>this.staffs = staffs
								 );
	}
}

