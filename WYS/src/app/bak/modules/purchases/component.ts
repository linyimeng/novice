import { Component } from '@angular/core';

@Component({
    selector:'purchases',
    template:`
    <div class="main">
		<div class="main-left">
			<h1>
				<span style="color:rgb(164,74,140)">s</span>c
			</h1>

			<div class="list">
				<div class="ultitle">进货</div>
				<ul>
					<li routerLink='/purchases/goods' routerLinkActive="active"><a>商品</a></li>
					<li routerLink='/purchases/supplier' routerLinkActive="active"><a>供应商</a></li>
					<li routerLink='/purchases/purchaseorder' routerLinkActive="active"><a>进货单</a></li>
				</ul>
				<div class="ultitle">报表</div>
				<ul>
					<li routerLink='/purchases/reports/purchaseorders' routerLinkActive="active"><a>商品进货报表</a></li>
				</ul>
				
			</div>
			<div class="footer">欢迎使用</div>
		</div>
		<div class="main-right" >
			<router-outlet></router-outlet>
		</div>
    </div>
    `
})

export class PurchasesComponent {

}