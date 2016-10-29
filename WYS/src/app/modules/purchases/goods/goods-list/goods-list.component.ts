import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { GoodsService } from '../../../wysservices/goods.service';

@Component({
   
   selector: 'goods-list',
   templateUrl: 'goods-list.component.html'
})
export class GoodsListComponent{
    goodss:any;

    constructor(
        private _goodsService:GoodsService,
        private router:Router
    ){}

    ngOnInit() {
        this._goodsService.get_goods_list().subscribe(
            goodss=>{
                console.log(goodss);
                for(let i in goodss){
                    goodss[i].static_attr = JSON.parse(goodss[i].static_attr);
                }
                this.goodss = goodss;
                console.log(this.goodss);
            },
            error=>alert(error)
        );
    }
}

