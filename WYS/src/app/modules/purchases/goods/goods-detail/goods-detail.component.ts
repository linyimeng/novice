import { Component,OnInit } from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';
import { FormArray }   from '@angular/forms';
import { GoodsService } from '../../../wysservices/goods.service';

import { Goods } from '../goods';
import { StaticAttr } from '../goods';
@Component({
   selector: 'goods-detail',
   templateUrl: 'goods-detail.component.html'
})

export class GoodsDetailComponent implements OnInit {
    goods:Goods = new Goods(null,null,null,null,null,null,null,null,null,null,null);
    static_attr:StaticAttr = new StaticAttr(null,null);
    constructor(
        private _goodsService:GoodsService,
        private router:Router,
        private activatedRoute:ActivatedRoute
    ){}
    
    ngOnInit() {
        this.activatedRoute.params.forEach(
            params=>{
                let pk= +params['pk'];
                this._goodsService.get_goods_detail(pk).subscribe(
                    goods=>{
                        this.static_attr = JSON.parse(goods.static_attr);
                        this.goods = goods;    
                    },
                    error=>alert(error)
                );
            },
        )
    }

    save_goods() {
        this.goods.static_attr = JSON.stringify(this.static_attr);
        let pk = this.goods.pk;
        let json = JSON.stringify(this.goods);
        this._goodsService.put_update_goods(pk,json).subscribe(
            goods=>{
                this.router.navigate(['/purchases/goods/list']);
            },
            error=>alert(error)
        );
    }
}

