import { Component,Input,OnInit } from '@angular/core';


import { OrderService } from '../../../wysservices/order.service';
import { GoodsService } from '../../../wysservices/goods.service';
import { OrderDetail,Order } from '../../model';

export class Item{
  constructor(
    public text,
    public id
  ){}
}
@Component({
   selector: 'purchaseorders-create',
   templateUrl: 'create.html',
   styles:[`
   `],
   providers:[OrderService]
})
export class PurchaseOrdersCreateComponent implements OnInit{

    datetime:string;
    order:Order = new Order(null,null,null,null,null,null,null,null);
    details:any = new Array;
    goodss:any;

    constructor(
        private _orderService:OrderService,
        private _goodsService:GoodsService
    ){}

    ngOnInit(){
        this.order.ordercode = this._orderService.get_ordercode();
        this.datetime = new Date().toLocaleString();
        this._goodsService.list().subscribe(
          goodss=>{
              this.goodss = goodss;
              this.set_items(goodss);
              this.init_detail();
          },
          error=>alert(error)
        );
    }
  
  init_detail(){
    let detail = new OrderDetail(null,null,null,null,null,null);
    this.details.push(detail);
  }
  save_order() {
      this.order.detail = JSON.stringify(this.details);
      let json = JSON.stringify(this.order);
      console.log(json);
  }

  setsupplierPk(pk) {
      this.order.company = Number(pk);
  }

  /** 设置商品下拉可选列表 */
  set_items(goodss:any) {
    let items:any = new Array;
    let a = 0;
    for(let i of goodss) {
      let item=new Item(null,null);
      item.id = i.pk;
      item.text = i.name;
      items[a] = item;
      a = a+1;
    }
    console.log(items);
    this.items = items;
  }

  /** 操作细节 */
  onchose(obj) {
    console.log(obj);
  }



  
  /** 下拉插件 */
  public items:any;

  private value:any = {};

  public selected(value:any):void {
    console.log('Selected value is: ', value);
  }

  public removed(value:any):void {
    console.log('Removed value is: ', value);
  }

  public typed(value:any):void {
    console.log('New search input: ', value);
  }

  public refreshValue(value:any):void {
    this.value = value;
  }
}
