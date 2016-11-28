import { Injectable } from '@angular/core';

import { Router,CanActivate,NavigationExtras } from '@angular/router';

/**
 * 验证token是否存在
 */
@Injectable()
export class AuthGuard implements CanActivate {
    constructor(private router:Router) { }
    canActivate() {
        console.log('守卫');
        let token=sessionStorage.getItem('wystoken');
        if(token) {
            return true;
        } else {
            this.router.navigate(['/login']);
            return false;
        }
    }
}
