import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   moduleId: module.id,
   selector: 'setting-users-right-title',
   templateUrl: 'setting-users-right-title.component.html'
})
export class GoodsRightComponent {
    constructor(
        private router:Router
    ) {}

    show_users_create() {
        this.router.navigate(['/setting/users/create']);
    }
}

