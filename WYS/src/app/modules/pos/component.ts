import { Component } from '@angular/core';

@Component({
    selector:'sales',
    template:`
    <div class="main">
		<!--
		<div class="main-left">
			<h1>
				<span style="color:rgb(164,74,140)">s</span>c
			</h1>

			<div class="list">
				<div class="ultitle" routerLink='/pos/retail'>零售</div>
			</div>
			<div class="footer">欢迎使用</div>
		</div>
		-->
		<div class="main-right">
			<router-outlet></router-outlet>
		</div>
    </div>
    `
})
export class PosComponent {

}