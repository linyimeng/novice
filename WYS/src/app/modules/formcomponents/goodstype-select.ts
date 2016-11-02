import { Component,OnInit,Input,Output,EventEmitter } from '@angular/core';
import { Router } from '@angular/router';

import { GoodsService } from '../wysservices/goods.service';

@Component({
   selector: 'goodstypeSelect',
   template: `
        <select [(ngModel)]="pk" (change)="onChange($event.target.value)">
            <option [value]="type.pk" *ngFor="let type of goodstypes">{{type.name}}</option>
        </select>
   `,
   providers:[ GoodsService ],
})
export class GoodstypeSelectComponent implements OnInit{
    
    @Output() outputpk = new EventEmitter<string>();
    pk:string = null;
    @Input() inputpk:any;

    goodstypes:any;

    constructor(
        private _goodstypeService:GoodsService
    ) { }

    ngOnInit() {
        this._goodstypeService.get_goods_type().subscribe(
            goodstypes=>{
                this.goodstypes=goodstypes;
                setTimeout(()=>{
                    this.pk=this.inputpk;
                    console.log(this.pk);
                },60);
            },
            error=>alert(error)
        );
    }
    onChange(pk) {
        this.outputpk.emit(pk);
    }
}

