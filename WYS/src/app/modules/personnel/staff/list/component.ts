import { Component,OnInit} from '@angular/core';
import { Router } from '@angular/router';

import { StaffService } from '../../../wysservices/staff.service';

@Component({
   
   selector: 'staff-list',
   templateUrl: 'list.html',
   providers:[StaffService]
})
export class StaffListComponent implements OnInit{
    staffs:any;

	constructor(
		private staffservice:StaffService,
		private router:Router
	) { }

	ngOnInit() {
		this.get_emp_list();
	}

	get_emp_list() {
		return this.staffservice.list()
							    .subscribe(
									 staffs=>this.staffs = staffs
								 );
	}
}

