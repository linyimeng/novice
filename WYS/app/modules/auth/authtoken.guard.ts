import { Injectable } from '@angular/core';

import { Router,CanActivate,NavigationExtras } from '@angular/router';
import { LoginComponent } from './login.component';
/**
 * 验证token是否存在
 */
@Injectable()
export class AuthTokenGuard implements CanActivate {
    constructor(private router:Router) { }
    canActivate() {
        let token=localStorage.getItem('wystoken');
        if(token) {
            return true;
        } else {
            //this.router.navigate([LoginComponent]);
            return true;
        }
    }
}
