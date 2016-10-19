import { Component } from '@angular/core';

@Component({
    moduleId:module.id,
    selector:'department',
    template:`
    <div class="main">
		<!-- 公共部分需模块化，待模块多后统一重新设计修改 -->
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
				<department-title></department-title>
			</div>
			<div class="content">
				<department-content></department-content>
			</div>
		</div>
    </div>
    `
})

export class DepartmentComponent {

}