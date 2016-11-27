import { Component } from '@angular/core';

@Component({
   selector: 'retail',
   template: `
   <!--零售
    <div class="title">
        <div class="left">零售</div>
        <div class="right">
            <span class="iconfont">&#xe638;</span>
            <input type="text">
        </div>
        
        <span class="action">动作<i class="iconfont">&#xe696;</i></span>
    </div>
    -->
    <router-outlet></router-outlet>
   `
})
export class RetailComponent {

}