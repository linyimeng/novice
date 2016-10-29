import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http,Headers,RequestOptions } from '@angular/http';

@Injectable()
export class DepartmentService extends BaseService {
    private GET_DEPARTMENT_LIST_URL = '/api/staff/departments.json';
    private GET_DEPARTMENT_DETAIL_URL = '/api/staff/departments/';
    private PUT_DEPARTMENT_URL = '/api/staff/departments/';
    private POST_DEPARTMENT_CREATE_URL = '/api/staff/departments.json';

    constructor(
        http:Http
    ) { super(http); }

    /** 获取部门列表 */
    get_department_list() {
        return this.http.get(this.get_requesr_url(this.GET_DEPARTMENT_LIST_URL),this.get_auth_header())
                 .map(this.extractData)
                 .catch(this.httpError);
    }

    /** 获取单个部门 */
    get_department_detail(pk:number) {
        let detailUrl = this.get_requesr_url(this.GET_DEPARTMENT_DETAIL_URL) + String(pk) + '.json';
        console.log(detailUrl);
        return this.http.get(detailUrl,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    /** 创建部门 */
    post_create_department(json:string) {
        return this.http.post(this.get_requesr_url(this.POST_DEPARTMENT_CREATE_URL),json,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    /** 更新一整个部门put */
    put_update_department(pk,json:string) {
        let updateUrl = this.get_requesr_url(this.PUT_DEPARTMENT_URL) + String(pk) + '.json';
        return this.http.put(updateUrl,json,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
}