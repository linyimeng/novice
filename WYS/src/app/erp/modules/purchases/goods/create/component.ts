import { Component,OnInit} from '@angular/core';
import { Router } from '@angular/router';

import { GoodsService } from '../../../../../services/goods.service';
import { TypeattrService } from '../../../../../services/typeattr.service';

export class Goods{
    constructor(
        public type,
        public gsav
    ){}
}

@Component({
   selector: 'goods-create',
   templateUrl: 'create.html'
})
export class GoodsCreateComponent{
    imgurl = '/assets/img/mr.png';
    other_attrs:any;
    goodstype:any = 1;
    constructor(
        private _goodsService:GoodsService,
        private _typeattrService:TypeattrService,
        private router:Router
    ){}

    ngOnInit() {
        this.get_static_attr_list();
    }

    /** 得到用户自定义属性 */
    get_static_attr_list(){
        this._typeattrService.get_attr_list('s',this.goodstype).subscribe(
            attr_list=>{
                this.other_attrs = attr_list.filter(attr=>attr.type=='s');
                console.log(this.other_attrs);
            },
            error=>alert('获取属性列表失败\n'+error)
        );
    }

    /** 保存新建的商品 */
    save_goods(form){
        /** gsav必须转化为字符串格式 */
        form.value.is_active = true;
        let gsav:string = JSON.stringify(form.value);
        let goods:Goods = new Goods(this.goodstype,gsav);
        let json = JSON.stringify(goods);
        console.log(json);
        this._goodsService.create(json).subscribe(
            goods=>{
                console.log("ok!"+JSON.stringify(goods));
                this.router.navigate(['/purchases/goods/list']);
            },
            error=>alert(error)
        );
    }

    setgoodstype(pk) {
        this.goodstype = pk;
        this.get_static_attr_list();
        console.log(pk);
    }

    setimgurl(url){
        this.imgurl = url;
    }
}
