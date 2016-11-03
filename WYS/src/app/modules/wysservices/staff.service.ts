import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http } from '@angular/http';

@Injectable()
export class StaffService extends BaseService {
    protected get_url = '/api/staff/emps.json';
    protected retrieve_url = '/api/staff/emp/';
    protected post_url = '/api/staff/emp.json';

    protected retrieve_user_url = '/api/staff/emp/user/';
    constructor(
        http:Http
    ) { super(http); }

    get_user_staff(uid:number){
        let url = this.get_requesr_url(this.retrieve_user_url) + String(uid) + '.json';
        return this.http.get(url,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
}