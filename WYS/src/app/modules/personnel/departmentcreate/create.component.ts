import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DepartmentService } from '../../wysservices/department.service';

export class Department {
    constructor(
        public name:string,
        public superiors: string,
        public manager: string,
		public remark: string
    ){}
}

@Component({
	
	selector: 'department-create',
	templateUrl: 'create.html',
	providers:[DepartmentService]
})

export class  DepartmentCreateComponent implements OnInit{
	department:Department;
	constructor(
		private _departmentService:DepartmentService,
		private router:Router
	) {}

	ngOnInit() {
		this.department = new Department('','','','');
	}

	save_department() {
        let json = JSON.stringify(this.department);
        this._departmentService.post_create_department(json).subscribe(
            department=> {
                    console.log(JSON.stringify(department));
					this.router.navigate(['/personnel/department/list']);
                 },
            error=>{alert(error)},
        )
    }
}


