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
    public batch,
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
    isshow:boolean;

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
        let index = this.get_index(detail);
        let goods = this.goodss.find(goods=>goods.gpk==value);
        this.details[index].gpk = goods.gpk;
        this.details[index].inventory = goods.inventory;
        this.details[index].goodsname = goods.gsav.name;
        this.details[index].unit = goods.gsav.unit;
        this.details[index].specification = goods.gsav.specification;
        this.details[index].manufacturer = goods.gsav.manufacturer;
        this.details[index].batch = goods.gdav.batch;
        this.details[index].validity = goods.gdav.validity;
        this.details[index].price = goods.gsav.saleprice;
        this.details[index].quantity = 1;
        this.set_total();
    }
    /** 设置单个商品数量 */
    set_quantity(detail,value){
        let index = this.get_index(detail);
        this.details[index].quantity = value;
        console.log(this.details[index].quantity);
        this.set_total();
    }
    /** 设置单个商品价格 */
    set_price(detail,value) {
        let index = this.get_index(detail);
        this.details[index].price = value;
        this.set_total();
    }

    /** 计算总数量和总价 */
    set_total(){
        let total_price = 0;
        let total_quantity = 0;
        for(let detail of this.details) {
            total_quantity = total_quantity + Number(detail.quantity);total_price = total_price + (Number(detail.price) * Number(detail.quantity));
        }
        this.order.totalprice = total_price;
        this.order.totalquantity = total_quantity;
    }

    /** 结帐 */
    checkout() {
        /** 订单主体 */
        let ordercode = this._orderService.get_ordercode('RO');
        let order:Order = new Order(ordercode,null,null,null,2,null,Number(localStorage.getItem('eid')));
        order.totalprice = this.order.totalprice;
        order.totalquantity = this.order.totalquantity;
        /** 订单详情 */
        let details = new Array;
        for(let d of this.details) {
            let detail:OrderDetail = new OrderDetail(null,null,null,null,null,null);
            let goods = this.goodss.find(goods=>goods.gpk==d.gpk);
            detail.gdav = JSON.stringify(goods.gdav);
            detail.gsav = JSON.stringify(goods.gsav);
            detail.goods = d.gpk;
            detail.order = ordercode;
            detail.price = d.price;
            detail.quantity = d.quantity;
            details.push(detail);
        }
        let save_order:SaveOrder = new SaveOrder(order,details);
        let json = JSON.stringify(save_order);
        console.log(json);
        this._orderService.create(json).subscribe(
            order=>{
                this.details
            }
        );
    }

    /** 获取当前元素索引值 */
    get_index(current){
        let obj = this.details;
        for (var i = 0;i < obj.length; i++) {
        if (obj[i] == current) {
            return i;
        }
        }
    }
    show(){
        this.isshow = true;
    }
    no_show() {
        this.isshow = false;
    }
}

