import { Component,OnInit} from '@angular/core';
import { Router } from '@angular/router';

import { GoodsService } from '../../../wysservices/goods.service';
import { TypeattrService } from '../../../wysservices/typeattr.service';
@Component({
   
   selector: 'goods-create',
   templateUrl: 'create.html'
})
export class GoodsCreateComponent{
    static_attrs:any;
    goodstype:any = 1;
    constructor(
        private _goodsService:GoodsService,
        private _typeattrService:TypeattrService,
        private router:Router
    ){}

    ngOnInit() {
        this.get_static_attr_list();
    }

    get_static_attr_list(){
        this._typeattrService.get_attr_list('static',this.goodstype).subscribe(
            attr_list=>{this.static_attrs = attr_list;console.log(attr_list)},
            error=>alert('获取属性列表失败\n'+error)
        );
    }
    save_goods(form){
        form.value.static_attr = JSON.stringify(form.value.static_attr);
        form.value.type = this.goodstype;
        let json = JSON.stringify(form.value);
        /*console.log(json);*/
        this._goodsService.create(json).subscribe(
            goods=>{
                console.log("ok!"+JSON.stringify(goods));
                this.router.navigate(['/purchases/goods/list']);
            },
            error=>alert(error)
        )
    }
    setgoodstype(pk) {
        this.goodstype = pk;
        this.get_static_attr_list();
        console.log(pk);
    }
}
