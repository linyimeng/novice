import { Component,OnInit } from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';
import { DepartmentService } from '../../../wysservices/department.service';

export class Department {
    constructor(
        public pk:number,
        public name:string,
        public superiors: string,
        public manager: string,
		public remark: string
    ){}
}

@Component({
	
	selector: 'department-detail',
	templateUrl: 'detail.html',
	providers:[DepartmentService]
})

export class  DepartmentDetailComponent implements OnInit{
	department:Department = new Department(null,'','','','');
	constructor(
		private _departmentService:DepartmentService,
		private router:Router,
        private activatedroute:ActivatedRoute
	) {}

	ngOnInit() {
        this.activatedroute.params.forEach(
            params=>{
                let pk= +params['pk'];
                this._departmentService.retrieve(pk).subscribe(
                    department=>this.department=department,
                    error=>alert(error)
                );
            }
        );
	}
    
	save_department() {
        let json = JSON.stringify(this.department);
        let pk = this.department.pk;
        console.log(pk);
        this._departmentService.update(pk,json).subscribe(
            department=> {
                    console.log(JSON.stringify(department));
					this.router.navigate(['/personnel/department/list']);
                 },
            error=>{alert(error)},
        )
    }

    setdepartpk(pk) {
        this.department.superiors = pk;
        console.log(pk);
    }
}
