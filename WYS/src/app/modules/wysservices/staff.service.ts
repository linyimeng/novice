import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http } from '@angular/http';

@Injectable()
export class StaffService extends BaseService {
    protected get_url = '/api/staff/emps.json';
    protected retrieve_url = '/api/staff/emp/';
    protected post_url = '/api/staff/emp.json';

    constructor(
        http:Http
    ) { super(http); }
}