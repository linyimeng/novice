import { Component,OnInit } from '@angular/core';
import { Router,ActivatedRoute } from '@angular/router';
import { FormArray }   from '@angular/forms';
import { GoodsService } from '../../../wysservices/goods.service';
import { TypeattrService } from '../../../wysservices/typeattr.service';
import { Goods } from '../model';
@Component({
   selector: 'goods-detail',
   templateUrl: 'detail.html'
})

export class GoodsDetailComponent implements OnInit {
    goods:Goods = new Goods(null,null,null,null,null,null,null,null,null,null,null);
    static_attr:any;
    static_attrs:any;
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
                        this.static_attr = JSON.parse(goods.static_attr);
                        this.goods = goods;
                        this.get_static_attr_list();
                    },
                    error=>alert(error)
                );
            },
        )
    }

    get_static_attr_list(){
        this._typeattrService.get_attr_list('static',this.goods.type).subscribe(
            attr_list=>{
                this.static_attrs = attr_list;
                this.get_attr_and_value();
            },
            error=>alert('获取属性列表失败\n'+error)
        );
    }

    /** 整理json数据至attrs[0].value格式 */
    get_attr_and_value() {
        let attrs = new Array();
        for(let a in this.static_attrs){
            let key = this.static_attrs[a].logicname;
            let attr = new Array();
            attr['value'] = this.static_attr[key];
            attr['name'] = this.static_attrs[a].name;
            attr['logicname'] = this.static_attrs[a].logicname;
            attrs[a] = attr;
        }
        this.attravlues = attrs;
    }
    
    save_goods(goodsForm) {
        let a = JSON.stringify(goodsForm.value.static_attr);
        this.goods.static_attr = a;
        let pk = this.goods.pk;
        let json = JSON.stringify(this.goods);
        this._goodsService.update(pk,json).subscribe(
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

