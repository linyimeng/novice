import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   moduleId: module.id,
   selector: 'goods-right',
   templateUrl: 'goods-right.component.html'
})
export class GoodsRightComponent {
    constructor(
        private router:Router
    ) {}

    show_client_create() {
        this.router.navigate(['/purchases/client/create']);
    }
}

