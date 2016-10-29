import { Injectable } from '@angular/core';
import { Http,Headers,RequestOptions,Response } from '@angular/http';
import { Observable } from 'rxjs/Rx';
@Injectable()
export class BaseService {

    protected HOST = 'http://127.0.0.1:8000';

    constructor(protected http:Http) { }

    /**
     * 获取请求的URL
     */
    protected get_requesr_url(url:string):string {
        let request_url = this.HOST + url;
        return request_url;
    }

    /**
     * 获取可用的http请求头
     */
    protected get_auth_header():RequestOptions {
        let auth_token = 'Token 78cbff35c687a6a67da92df41d6cb2233f51e348';
        let headers = new Headers({ 'Content-Type': 'application/json','Authorization':auth_token});
        let options = new RequestOptions({ headers: headers });
        return options;
    }

    /**
     * 获取当前登录用户id
     */
    protected getuid() {
        let uid = 1;
        return uid;
    }

    /**
     * 提取返回的json数据
     */
    protected extractData(res: Response) {
        let body = res.json();
        return body || { };
    }

    /**
     * 捕获http请求中的异常
     */
    protected httpError (error: any) {
        let errMsg = (error.message) ? error.message :
        error.status ? `${error.status} - ${error.statusText}` : 'Server error';
        console.error(errMsg); // log to console instead
        return Observable.throw(errMsg);
    }
}