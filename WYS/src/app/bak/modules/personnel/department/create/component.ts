import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DepartmentService } from '../../../wysservices/department.service';

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
	department:Department = new Department('','','','');
	departments:any;
	constructor(
		private _departmentService:DepartmentService,
		private router:Router
	) {}

	ngOnInit() {
		this._departmentService.list().subscribe(
			departments=>this.departments = departments,
			error=>alert(error)
		);
	}

	save_department() {
        let json = JSON.stringify(this.department);
		console.log(json);
		
        this._departmentService.create(json).subscribe(
            department=> {
                    console.log(JSON.stringify(department));
					this.router.navigate(['/personnel/department/list']);
                 },
            error=>{alert(error)},
        );
    }

	setdepartmentPk(pk:string){
		this.department.superiors = pk;
	}
}


