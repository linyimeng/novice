import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DepartmentService } from '../../wysservices/department.service';

@Component({
	
	selector: 'department-content',
	templateUrl: 'departmentcontent.component.html',
	providers:[DepartmentService]
})
export class  DepartmentcontentComponent implements OnInit{
	departments:any;
	constructor(
		private _departmentService:DepartmentService,
		private router:Router
	) {}

	ngOnInit() {
		this.get_list();
	}

	get_list() {
		this._departmentService.get_department_list().subscribe(
			departments=>this.departments=departments,
			err=>alert('获取数据失败')
		)
	}

	gotodetail(pk){
		this.router.navigate(['/personnel/department',pk]);
	}
}


