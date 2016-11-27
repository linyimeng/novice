import { Component,OnInit } from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';
import { FormArray }   from '@angular/forms';
import { GoodsService } from '../../../wysservices/goods.service';
import { TypeattrService } from '../../../wysservices/typeattr.service';

class Gsav {
    constructor(
        public name,
        public specification,
        public unit,
        public barcode,
        public manufacturer,
        public saleprice,
        public is_active,
        public customid,
        public approvalnumber,
        public origin,
        public percent
    ){ }
}

class Detail {
    constructor(
        public pk,
        public type,
        public gsav:Gsav
    ){}
}

class Save_goods {
    constructor(
        public pk,
        public type,
        public gsav:string
    ){}
}
@Component({
   selector: 'goods-detail',
   templateUrl: 'detail.html'
})

export class GoodsDetailComponent implements OnInit {
    gsav:Gsav = new Gsav(null,null,null,null,null,null,null,null,null,null,null);
    goods:Detail = new Detail(null,null,this.gsav);
    other_attr:any;
    other_attrs:any;
    attravlues:any;
    constructor(
        private _goodsService:GoodsService,
        private _typeattrService:TypeattrService,
        private router:Router,
        private activatedRoute:ActivatedRoute
    ){}
    
    ngOnInit() {
        this.activatedRoute.params.forEach(
            params=>{
                let pk=params['pk'];
                this._goodsService.retrieve(pk).subscribe(
                    goods=>{
                        this.other_attr = goods.gsav;
                        this.goods.gsav = goods.gsav;
                        this.goods.pk = goods.pk;
                        this.goods.type = goods.type;
                        this.get_static_attr_list();
                    },
                    error=>alert(error)
                );
            },
        )
    }

    get_static_attr_list(){
        this._typeattrService.get_attr_list('s',this.goods.type).subscribe(
            attr_list=>{
                this.other_attrs = attr_list.filter(attr=>attr.type=='s');
                this.get_attr_and_value();
                console.log(this.attravlues);
            },
            error=>alert('获取属性列表失败\n'+error)
        );
    }

    /** 整理json数据至attrs[0].value格式 */
    get_attr_and_value() {
        let attrs = new Array();
        console.log(this.other_attr);
        console.log(this.other_attrs);
        for(let a in this.other_attrs){
            let key = this.other_attrs[a].keyname;
            let attr = new Array();
            attr['value'] = this.other_attr[key];
            attr['name'] = this.other_attrs[a].name;
            attr['keyname'] = this.other_attrs[a].keyname;
            attrs[a] = attr;
        }
        this.attravlues = attrs;
    }
    
    save_goods(goodsForm) {
        /** 商品是否可用 */
        goodsForm.value.is_active = true;
        let save_goods = new Save_goods(this.goods.pk,this.goods.type,JSON.stringify(goodsForm.value));
        let json = JSON.stringify(save_goods);
        console.log(json);
        this._goodsService.update(this.goods.pk,json).subscribe(
            goods=>{
                this.router.navigate(['/purchases/goods/list']);
            },
            error=>alert(error)
        );
    }

    /** 设置商品分类选项 */
    setgoodstype(pk) {
        this.goods.type = pk;
    }
}

