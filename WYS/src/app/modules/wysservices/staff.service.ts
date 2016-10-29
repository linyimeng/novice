import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http,Headers,RequestOptions } from '@angular/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class StaffService extends BaseService {
    private GET_EMP_LIST_URL = '/api/staff/emp.json';
    private GET_EMP_DETAIL_URL = '/api/staff/emp/';
    private POST_CREATE_EMP_URL = '/api/staff/emp.json';
    constructor(
        http:Http
    ) { super(http); }

    get_emp_list() {
        return this.http.get(super.get_requesr_url(this.GET_EMP_LIST_URL),super.get_auth_header())
                 .map(res=>super.extractData(res))
                 .catch(super.httpError);
    }

    get_emp_detail(pk) {
        let url =super.get_requesr_url(this.GET_EMP_DETAIL_URL) + String(pk) + '.json';
        return this.http.get(url,super.get_auth_header())
                        .map(super.extractData)
                        .catch(super.httpError);
    }

    post_create_emp(json:string) {
        return this.http.post(super.get_requesr_url(this.POST_CREATE_EMP_URL),json,super.get_auth_header())
                        .map(res=>super.extractData(res))
                        .catch(super.httpError);
    }

     /** 更新一整个员工对象put */
    put_update_emp(pk,json:string) {
        let updateUrl = super.get_requesr_url(this.GET_EMP_DETAIL_URL) + String(pk) + '.json';
        return this.http.put(updateUrl,json,super.get_auth_header())
                        .map(super.extractData)
                        .catch(super.httpError);
    }

}