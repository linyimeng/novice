import { Component } from '@angular/core';

@Component({
    moduleId:module.id,
    selector:'staff',
    template:`
    <div class="main">
		<div class="main-left">
		<h1>
			<span style="color:rgb(164,74,140)">s</span>c
		</h1>
		<div class="list">
			<staff-list></staff-list>
		</div>
		<div class="footer">欢迎使用</div>
		</div>

		<div class="main-right" >
			<div class="title">
				<staff-title></staff-title>
			</div>
			<div class="content">
				<staff-content></staff-content>
			</div>
		</div>
    </div>
    `

})

export class StaffComponent {

}