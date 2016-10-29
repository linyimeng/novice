import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

@Injectable()
export class AuthService {

    private AuthTokenUrl:string = 'http://127.0.0.1:8000/api/user/login.json';
    
    constructor(
        private http:Http
    ) { }

    get_auth_token() {
        let auth_token = '78cbff35c687a6a67da92df41d6cb2233f51e348';
        localStorage.setItem('wystoken',auth_token);
        localStorage.setItem('wysid','1');
        return auth_token;
    }
}