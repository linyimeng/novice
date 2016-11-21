import { Component,OnInit } from '@angular/core';

import { GoodsService } from '../../../wysservices/goods.service';
import { OrderService } from '../../../wysservices/order.service';

import { OrderDetail,Order } from '../../../purchases/model';

class SaleOrder{
    constructor(
        public totalprice:number,
        public totalquantity:number,
        public smallchange:number
    ){}
}

class Detail{
  constructor(
    public gpk,
    public goodsname,
    public specification,
    public quantity,
    public price,
    public batch_number,
    public validity,
    public production_date,
    public unit,
    public manufacturer,
    public inventory
  ){}
}
class SaveOrder {
  constructor(
    public order,
    public detail
  ){}
}


/** 商品input下拉 */
class Item {
    constructor(
        public value:string,
        public name:string
    ){}
}
@Component({
   selector: 'pos',
   templateUrl: 'retail.html',
   providers:[GoodsService,OrderService]
})

export class RetailContentComponent implements OnInit{
    order:SaleOrder = new SaleOrder(0,0,0);
    goodss:any;
    details:any = new Array;

    /** input商品下拉 */
    items = new Array;

    constructor(
        private _goodsService:GoodsService,
        private _orderService:OrderService
    ){}

    ngOnInit() {
        this._goodsService.get_wms_goods().subscribe(
            goodss=>{
                this.goodss=goodss;
                this.set_items();
                console.log('goodss');
                console.log(this.goodss);
            },
        );
    }

    /** 设置商品下拉列表 */
    set_items(){
        for(let goods of this.goodss){
            let item:Item = new Item(goods.gpk,goods.gsav.name);
            this.items.push(item);
        }
        console.log(this.items);
    }

    /** 添加一个空行 */
    init_details() {
        let detail = new Detail(null,null,null,null,null,null,null,null,null,null,null);
        this.details.push(detail);
    }

    chose_goods(detail,value) {

    }

}

