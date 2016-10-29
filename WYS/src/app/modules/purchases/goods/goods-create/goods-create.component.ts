import { Component,OnInit} from '@angular/core';
import { Router } from '@angular/router';

import { GoodsService } from '../../../wysservices/goods.service';
import { TypeattrService } from '../../../wysservices/typeattr.service';
@Component({
   
   selector: 'goods-create',
   templateUrl: 'goods-create.component.html'
})
export class GoodsCreateComponent{
    static_attrs:any;
    constructor(
        private _goodsService:GoodsService,
        private _typeattrService:TypeattrService,
        private router:Router
    ){}

    ngOnInit() {
        this._typeattrService.get_attr_list('static').subscribe(
            attr_list=>{this.static_attrs = attr_list;console.log(attr_list)},
            error=>alert('获取属性列表失败\n'+error)
        );
    }

    save_goods(form){
        form.value.static_attr = JSON.stringify(form.value.static_attr);
        let json = JSON.stringify(form.value);
        this._goodsService.post_create_goods(json).subscribe(
            goods=>{
                console.log("ok!"+JSON.stringify(goods));
                this.router.navigate(['/purchases/goods/list']);
            },
            error=>alert(error)
        )    
    }
}
