import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   moduleId: module.id,
   selector: 'warehouse-loss-right-title',
   templateUrl: 'warehouse-loss-right-title.component.html'
})
export class GoodsRightComponent {
    constructor(
        private router:Router
    ) {}

    show_goods_loss_create() {
        this.router.navigate(['/purchases/goodsloss/create']);
    }
}

