import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http } from '@angular/http';

@Injectable()
export class DepartmentService extends BaseService {
    protected get_url = '/api/employee/departments.json';
    protected retrieve_url = '/api/employee/departments/';
    protected put_url = '/api/employee/departments/';
    protected post_url = '/api/employee/departments.json';

    constructor(
        http:Http
    ) { super(http); }
    
    /** 获取相关部门的职位 */
    get_department_jobs(dpk:string){
        let url = '/api/employee/djobs/'+ String(dpk) + '.json';
        return this.http.get(this.get_requesr_url(url),this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
}