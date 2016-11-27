import { Component } from '@angular/core';

@Component({
    
    selector:'setting',
    template:`
    <div class="main">
		<div class="main-left user">
			<h1>
				<span style="color:rgb(164,74,140)">s</span>c
			</h1>

			<div class="list">
				
				<div class="ultitle">用户</div>
				<ul>
					<li class="active"><a href="">所有用户</a></li>	
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
export class SettingComponent {

}