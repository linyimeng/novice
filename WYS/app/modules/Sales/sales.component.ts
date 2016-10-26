import { Component } from '@angular/core';

@Component({
    moduleId:module.id,
    selector:'sales',
    template:`
    <div class="main">
		<div class="main-left">
			<h1>
				<span style="color:rgb(164,74,140)">s</span>c
			</h1>

			<div class="list">
				<div class="ultitle">销售</div>
				<ul>
					<li class="active"><a>客户</a></li>
					<li><a href="">销售单</a></li>
				</ul>
				<div class="ultitle">报表</div>
				<ul>
					<li><a href="">日期销售报表</a></li>
					<li><a href="">商品销售报表</a></li>
					<li><a href="">客户销售报表</a></li>
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
export class SalesComponent {

}