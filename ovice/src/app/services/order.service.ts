import { Injectable } from '@angular/core';
import { BaseService } from './base.service';
import { Http } from '@angular/http';
@Injectable()
export class OrderService extends BaseService {

    protected post_url = '/api/order/create.json';
    protected get_list_io_url = '/api/order/list/io/';
    protected get_detail_url = '/api/order/';

    constructor(
        http:Http
    ) { super(http); }
    

    get_ordergoods_list(io:string) {
        let url = this.get_requesr_url('/api/order/ordergoods/') + io + '.json';
        return this.http.get(url,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
    /** 根据订单号得到订单详情 */
    get_order_detail(ordercode:string) {
        let url = this.get_requesr_url(this.get_detail_url) + ordercode + '.json';
        return this.http.get(url,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
    /** 得到io订单：i为入库单，o为出库单 */
    get_list_io(io:string) {
        let url = this.get_requesr_url(this.get_list_io_url) + io + '.json';
        return this.http.get(url,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }
    /** 获取单号 */
    get_ordercode(type:string) {
        let uid = sessionStorage.getItem('user');
        let timestamp = new Date().getTime();
        let ordercode = uid + timestamp;
        ordercode = type + ordercode;
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