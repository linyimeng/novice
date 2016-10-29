import { Component } from '@angular/core';

@Component({
    moduleId:module.id,
    selector:'warehouse',
    template:`
   	<div class="main">
		<div class="main-left">
			<h1>
				<span style="color:rgb(164,74,140)">s</span>c
			</h1>

			<div class="list">
				<div class="ultitle">仓库</div>
				<ul>
					<li routerLink="/warehouse/loss" routerLinkActive="active"><a>损耗录入</a></li>
					
				</ul>
				<div class="ultitle">报表</div>
				<ul>
					<li routerLink="/warehouse/reports/goodslastreports" routerLinkActive="active"><a>商品剩余报表</a></li>
					<li routerLink="/warehouse/reports/warehouselastreports" routerLinkActive="active"><a>各仓库剩余报表</a></li>
				</ul>
			</div>
			<div class="footer">欢迎使用</div>
		</div>
		<div class="main-right">
			<router-outlet></router-outlet>
		</div>
    </div>
    `
})
export class WarehouseComponent {

}