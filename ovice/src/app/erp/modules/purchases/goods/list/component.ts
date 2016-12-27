import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { GoodsService } from '../../../../../services//goods.service';

@Component({
   selector: 'goods-list',
   templateUrl: 'list.html',
})
export class GoodsListComponent{
    goodss:any;
    constructor(
        private _goodsService:GoodsService,
        private router:Router
    ){}

    ngOnInit() {
        this._goodsService.list().subscribe(
            goodss=>{
                console.log(goodss);
                this.goodss = goodss;
                console.log(this.goodss);
            },
            error=>alert(error)
        );
    }
}

