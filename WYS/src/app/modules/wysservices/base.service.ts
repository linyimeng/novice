import { Injectable } from '@angular/core';
import { Http,Headers,RequestOptions,Response } from '@angular/http';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class BaseService {

    protected HOST = 'http://127.0.0.1:8000';

    protected post_url:string;
    protected put_url:string;
    protected delete_url:string;
    protected get_url:string;
    protected retrieve_url:string;

    constructor(protected http:Http) { }

    /**
     * 获取请求的URL
     */
    protected get_requesr_url(url:string):string {
        let request_url = this.HOST + url;
        return request_url;
    }

    /** 获取列表 */
    public list() {
        return this.http.get(this.get_requesr_url(this.get_url),this.get_auth_header())
                 .map(this.extractData)
                 .catch(this.httpError);
    }

    /** 获取单个 */
    public retrieve(pk:number) {
        let url = this.get_requesr_url(this.retrieve_url) + String(pk) + '.json';
        return this.http.get(url,this.get_auth_header())
                 .map(this.extractData)
                 .catch(this.httpError);
    }

    /** 增加，创建 */
    public create(json:string) {
        return this.http.post(this.get_requesr_url(this.post_url),json,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    /** 更新 */
    public update(pk:number,json:string) {
        let url:string;
        if(typeof(this.put_url)=='undefined') {
            url = this.get_requesr_url(this.retrieve_url) + String(pk) + '.json';
        } else {
            url = this.get_requesr_url(this.put_url) + String(pk) + '.json';
        }
        return this.http.put(url,json,this.get_auth_header())
                        .map(this.extractData)
                        .catch(this.httpError);
    }

    /**
     * 获取可用的http请求头
     */
    protected get_auth_header():RequestOptions {
        let wystoken = sessionStorage.getItem('wystoken');
        let auth_token = 'Token ' + wystoken;
        let headers = new Headers({ 'Content-Type': 'application/json','Authorization':auth_token});
        let options = new RequestOptions({ headers: headers });
        return options;
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