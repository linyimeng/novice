import { Component,OnInit } from '@angular/core';
import { GoodsService } from '../../../../wysservices/goods.service';

@Component({   
   selector: 'goods-last-reports',
   templateUrl: 'goods-last-reports.html'
})
export class GoodsLastReportsContentComponent implements OnInit{
    goodss:any;
    filtered_data:any;
    totalinventory:number;
    constructor(
        private _goodsService:GoodsService
    ){}

    ngOnInit(){
        this._goodsService.get_wms_goods().subscribe(
            goodss=>{
                this.goodss = goodss;
                this.filtered_data = goodss;
                this.set_total();
            },
            error=>alert(error)
        );
    }

    set_total(){
        let totalinventory=0;
        for(let goods of this.filtered_data) {
            totalinventory = totalinventory + goods.inventory;
        }
        this.totalinventory = totalinventory;
    }

    filter_goodsname(value) {
        console.log(value);
        this.filtered_data = this.goodss.filter(item=>
            item.gsav.name.indexOf(value)!=-1);
        this.set_total();
    }
}
