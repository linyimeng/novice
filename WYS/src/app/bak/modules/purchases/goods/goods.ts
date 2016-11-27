import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   
   selector: 'goods',
   templateUrl: 'goods.html'
})
export class GoodsComponent {
    constructor(
        private router:Router
    ) {}

    show_goods_create() {
        this.router.navigate(['/purchases/goods/create']);
    }
}

