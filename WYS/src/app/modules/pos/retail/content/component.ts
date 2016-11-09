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
class Item{
    constructor(
        public id,
        public text
    ){}
}

class Detail{
  constructor(
    public gpk,
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
    constructor(
        private _goodsService:GoodsService,
        private _orderService:OrderService
    ){}

    ngOnInit() {
        this._goodsService.get_wms_goods().subscribe(
            goodss=>{
                this.goodss=goodss;
                this.set_items(goodss);
            },
        );
    }

    set_items(goodss:any) {
        let items:any = new Array;
        let a = 0;
        for(let i of goodss) {
            let item=new Item(null,null);
            item.id = i.goods;
            item.text = i.name;
            items[a] = item;
            a = a+1;
        }
        console.log(items);
        this.items = items;
    }

    public items:any;

    private value:any;

    public selected(value:any,detail):void{
        let index = this.index(detail);
        let goods = this.goodss.find(goods => goods.goods === value.id);
        this.details[index].gpk = goods.goods;
        this.details[index].specification = goods.specification;
        this.details[index].unit = goods.unit;
        this.details[index].manufacturer = goods.manufacturer;
        this.details[index].price = goods.salesprice;
        this.details[index].quantity = 1;
        this.details[index].batch = goods.batch;
        this.details[index].validity = goods.validity;
        this.details[index].inventory = goods.inventory;
        this.set_total();
        console.log(value);
    }

    set_total(){
        let totalprice = 0;
        let totalquantity = 0;
        for(let i of this.details){
            totalprice = totalprice + Number(i.price);
            totalquantity = totalquantity + Number(i.quantity);
        }
        this.order.totalprice = totalprice;
        this.order.totalquantity = Number(totalquantity);
        console.log(totalprice);
    }

    init_details(){
        let detail = new Detail(null,null,null,null,null,null,null,null,null,null);
        this.details.push(detail);
        console.log(this.details);
    }

    /** 获取当前元素索引值 */
    index(current){
        let obj = this.details;
        for (var i = 0;i < obj.length; i++) {
        if (obj[i] == current) {
            return i;
        }
        }
    }
    public removed(value:any,detail):void {
        let index = this.index(detail);
        this.details.splice(index,1);
        console.log('Removed value is: ', value);
    }

    public typed(value:any):void {
    console.log('New search input: ', value);
    }

    public refreshValue(value:any):void {
    this.value = value;
    }

    show(){
        this.isshow = true;
    }

    checkout() {
        this.set_total();
        let order:Order = new Order(null,null,null,null,null,null,null)
        //生成主体订单
        order.ordercode = this._orderService.get_ordercode('O');
        order.type = 2;
        order.totalprice = Number(this.order.totalprice.toFixed(8));
        order.totalquantity = Number(this.order.totalquantity.toFixed(2));
        order.creator = Number(sessionStorage.getItem('eid'));
        //订单详情
        let orderdetail = new Array;
        let i = 0;
        for(let detail of this.details) {
            let item:any = new OrderDetail(null,null,null,null,null,null,null,null,null);
            item.order = order.ordercode;
            item.goods = Number(detail.gpk);
            item.quantity = Number(detail.quantity);
            item.productiondate = detail.productiondate;
            item.batch = detail.batch;
            item.validity = detail.validity;
            item.price = Number(detail.price);
            orderdetail.push(item);
        }
        let save_order = new SaveOrder(order,orderdetail);
        let json = JSON.stringify(save_order);
        console.log(json);
        this._orderService.create(json).subscribe(
            order=>{
                console.log(order);
                this.isshow = false;
                this.sub_inventory();
                this.details = [];
            },
            error=>alert(error)
        )
    }

    set_smallchange(money:number) {
        let result = money - this.order.totalprice;
        if(result>0){
            this.order.smallchange = result;
        }
    }

    /** 减本地库存 */
    sub_inventory(){
        for(let detail of this.details) {
            let index = this.goodss.findIndex(goods => goods.goods === detail.gpk);
            this.goodss[index].inventory = Number(this.goodss[index].inventory) - Number(detail.quantity);
        }
    }

}

