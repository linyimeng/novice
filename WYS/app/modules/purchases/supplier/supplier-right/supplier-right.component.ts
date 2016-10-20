import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   moduleId: module.id,
   selector: 'goods-right',
   templateUrl: 'goods-right.component.html'
})
export class GoodsrightComponent {
    constructor(
        private router:Router
    ) {}

    showgoodscreate() {
        this.router.navigate(['/purchases/supplier/create']);
    }
}

