import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { GoodsService } from '../../../wysservices/goods.service';
import { TypeattrService } from '../../../wysservices/typeattr.service';
@Component({
   selector: 'goods-list',
   templateUrl: 'list.html',
   providers:[]
})
export class GoodsListComponent{
    goodss:any;
    attrs:any;
    constructor(
        private _goodsService:GoodsService,
        private _typeattrService:TypeattrService,
        private router:Router
    ){}

    ngOnInit() {
        this._goodsService.list().subscribe(
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
        // this._typeattrService.get_attr_list('static',1).subscribe(
        //     attrs=>{
        //         this.attrs = attrs;
        //         console.log(this.attrs);
        //     },
        //     error=>alert(error)
        // );
    }
}

