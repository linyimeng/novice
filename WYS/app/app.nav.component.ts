import { Component } from '@angular/core';

@Component({
    moduleId:module.id,
    selector:'wys-nav',
    template:`
        <nav>
            <ul>
                <li routerLink="/yg" routerLinkActive="activity" class="activity">
                    <a routerLink='/department'>员工</a>
                </li>
                <li routerLink="/jh">
                    <a href="#">进货</a>
                </li>
                <li routerLink="/xs">
                    <a href="#">销售</a>
                </li>
                <li routerLink="/ck">
                    <a href="#">仓库</a>
                </li>
                <li routerLink="/cw">
                    <a href="#">财务</a>
                </li>
                <li routerLink="/sz">
                    <a href="#">设置</a>
                </li>
            </ul>
            <div class="nav-left">
                <span class="iconfont">&#xe647;</span>
                <div class="user-div">
                    <span class="iconfont">&#xe621;</span>
                    <span class="user">admin</span>
                    <span class="iconfont triangle">&#xe696;</span>
                </div>
            </div>
        </nav>
    `
})

export class NavComponent {

}