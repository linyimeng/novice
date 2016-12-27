import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
	selector: 'erp-home',
	template: `
    <nav>
        <ul>
            <li routerLink="/staff" routerLinkActive="activity">
                <a>员工</a>
            </li>
            <li routerLink='/purchases' routerLinkActive="activity">
                <a >进货</a>
            </li>
            <li routerLink='/sales' routerLinkActive="activity">
                <a>销售</a>
            </li>
            <!--
            <li routerLink='/pos' routerLinkActive="activity">
                <a>零售</a>
            </li>
            -->
            <li routerLink='/warehouse' routerLinkActive="activity">
                <a>库存</a>
            </li>
            <!-- 财务模块暂不启用
            <li><a>财务</a></li>
            -->
            <!-- 暂无设置模块
            <li routerLink='/setting' routerLinkActive="activity">
                <a>设置</a>
            </li>
            -->
        </ul>
        <div class="nav-left">
            <span class="iconfont">&#xe647;</span>
            <div class="user-div">
                <span class="iconfont">&#xe621;</span>
                <span class="user">{{username}}</span>
                <span class="iconfont triangle">&#xe696;</span>
            </div>
        </div>
    </nav>
    <router-outlet></router-outlet>
	`,
})
export class ErpHomeComponent {

}
