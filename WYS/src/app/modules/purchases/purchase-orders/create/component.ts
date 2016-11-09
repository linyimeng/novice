import { Component,Input,OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { OrderService } from '../../../wysservices/order.service';
import { GoodsService } from '../../../wysservices/goods.service';
import { OrderDetail,Order } from '../../model';

export class Item{
  constructor(
    public text,
    public id
  ){}
}

class Detail{
  constructor(
    public gpk,
    public specification,
    public quantity,
    public price,
    public totalprice,
    public batch_number,
    public validity,
    public production_date,
    public unit,
    public manufacturer
  ){}
}

class SaveOrder {
  constructor(
    public order,
    public detail
  ){}
}


@Component({
   selector: 'purchaseorders-create',
   templateUrl: 'create.html',
   styles:[`
    input {border:none;outline:none;}
    .num {width:60px}
    .date_length {width:118px}
   `],
   providers:[OrderService]
})
export class PurchaseOrdersCreateComponent implements OnInit{

    datetime:string;
    order:Order = new Order(null,null,null,null,null,null,null);
    details:any = new Array;
    goodss:any;

    constructor(
        private _orderService:OrderService,
        private _goodsService:GoodsService,
        private router:Router
    ){}

    ngOnInit(){
        this.order.ordercode = this._orderService.get_ordercode('I');
        this.datetime = new Date().toLocaleString();
        this._goodsService.list().subscribe(
          goodss=>{
              this.goodss = goodss;
              this.set_items(goodss);
          },
          error=>alert(error)
        );
    }
  
  init_detail(){
    let detail = new Detail(null,null,0,0,null,null,null,null,null,null);
    this.details.push(detail);
    console.log(this.details);
  }
  delete_detail(detail){
    if(confirm('是否删除')){
      let index = this.index(detail);
      this.details.splice(index,1);
    } else {
      return;
    }
  }
  save_order() {
      if(!this.checkcompany()) return;
      this.set_total();
      let orderdetail = this.before_save_orderdetail();
      this.order.type = 1;
      this.order.creator = Number(sessionStorage.getItem('eid'));
      this.order.totalprice = Number(this.order.totalprice.toFixed(8));
      this.order.totalquantity = Number(this.order.totalquantity.toFixed(2));
      let save_order = new SaveOrder(this.order,orderdetail);
      let json = JSON.stringify(save_order);
      console.log(json);
      this._orderService.create(json).subscribe(
        order=>{
          this.router.navigate(['/purchases/purchaseorder/list']);
        },
        error=>alert(error)
      )
  }

  checkcompany() {
    if(typeof(this.order.company)=="object") {
      alert('供应商不能为空');
      return false;
    }
    return true;
  }

  before_save_orderdetail(){
    let orderdetail = new Array;
    let i = 0;
    for(let detail of this.details){
      let item:any = new OrderDetail(null,null,null,null,null,null,null,null,null);
      item.order = this.order.ordercode;
      item.goods = detail.gpk;
      item.validity = detail.validity;
      item.productiondate = detail.production_date;
      item.batch = detail.batch_number;
      item.quantity = Number(detail.quantity);
      item.price = Number(detail.price);
      orderdetail.push(item);
    }
    return orderdetail;
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

  /** 获取当前元素索引值 */
  index(current){
    let obj = this.details;
    for (var i = 0;i < obj.length; i++) {
      if (obj[i] == current) {
        return i;
      }
    }
  }


  
  /** 下拉插件 */
  public items:any;

  private value:any;

  public selected(value:any,detail):void {
    let index = this.index(detail);
    let goods = this.goodss.find(goods => goods.pk === value.id);
    this.details[index].gpk = goods.pk;
    this.details[index].specification = goods.specification;
    this.details[index].unit = goods.unit;
    this.details[index].manufacturer = goods.manufacturer;
    console.log(goods);
    console.log(value.id);
    console.log(this.details[index]);
    console.log('Selected value is: ', value);
  }
  /** 设置对应对象的数量 */
  set_quantity(quantity,detail) {
    console.log(quantity);
    let index = this.index(detail);
    this.details[index].quantity = quantity;
    this.details[index].totalprice = this.details[index].quantity * this.details[index].price;
    this.set_total();
  }
  /** 设置对应对象的价格 */
  set_price(price,detail) {
    console.log(price);
    let index = this.index(detail);
    this.details[index].price = price;
    this.details[index].totalprice = this.details[index].quantity * this.details[index].price;
    this.set_total();
  }
  /** 设置对应对象的批号 */
  set_batch_number(batch,detail){
    let index = this.index(detail);
    this.details[index].batch_number = batch;
  }
  /** 设置对应对象的有效期 */
  set_validity(validity,detail){
    let index = this.index(detail);
    this.details[index].validity = validity;
    console.log(validity);
  }

  /** 设置对应对象的生产日期 */
  set_production_date(production_date,detail) {
    let index = this.index(detail);
    this.details[index].production_date = production_date;
  }

  /** 重新计算总数量和总额 */
  set_total() {
    let totalprice = 0;
    let totalquantity = 0;
    for(let i of this.details){
      totalprice = totalprice + i.totalprice;
      totalquantity = totalquantity + i.quantity;
    }
    this.order.totalprice = totalprice;
    this.order.totalquantity = Number(totalquantity);
  }

  validate_num(num){
    let reg = new RegExp("^[0-9]*$");
    if(!reg.test(num)){  
        return false;  
    }
    return true;
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
