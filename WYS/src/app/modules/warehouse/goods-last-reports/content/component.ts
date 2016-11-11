import { Component,OnInit } from '@angular/core';
import { GoodsService } from '../../../wysservices/goods.service';

@Component({   
   selector: 'goods-last-reports',
   templateUrl: 'goods-last-reports.html'
})
export class GoodsLastReportsContentComponent implements OnInit{
    goodss:any;
    constructor(
        private _goodsService:GoodsService
    ){}

    ngOnInit(){
        this._goodsService.get_wms_goods().subscribe(
            goodss=>{
                this.goodss = goodss;
            },
            error=>alert(error)
        );
    }
}
