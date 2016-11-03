import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http } from '@angular/http';
@Injectable()
export class OrderService extends BaseService {

    protected post_url = '/api/order/create.json';

    constructor(
        http:Http
    ) { super(http); }
    
    get_ordercode() {
        let uid = sessionStorage.getItem('user');
        let timestamp = new Date().getTime();
        let ordercode = uid + timestamp;
        return ordercode;
    }

    get_datetime() {
        let date = new Date();
        // let year = date.getFullYear();
        // let month = date.getMonth();
        // let ddate = date.getDate();
        // let hours = date.getHours();
        // let minutes=date.getMinutes();
        // let seconds=date.getSeconds();
        let datetime = date.toLocaleString();
        return datetime;
    }

}