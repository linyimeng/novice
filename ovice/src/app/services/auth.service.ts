import { Injectable } from '@angular/core';
import { Http,Response,RequestOptions,Headers } from '@angular/http';
import { Observable } from 'rxjs/Rx';
@Injectable()
export class AuthService {

    private AuthTokenUrl:string = 'http://127.0.0.1:8000/api/user/login.json';
    
    constructor(
        private http:Http
    ) { }

    get_auth_token(json:string) {
        return this.http.post(this.AuthTokenUrl,json,this.get_header())
                 .map(this.extractData)
                 .catch(this.httpError);
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

    /**
     * 获取可用的http请求头
     */
    protected get_header():RequestOptions {
        let headers = new Headers({ 'Content-Type': 'application/json'});
        let options = new RequestOptions({ headers: headers });
        return options;
    }
}