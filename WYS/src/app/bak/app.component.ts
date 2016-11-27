import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { StaffService } from './modules/wysservices/staff.service';

@Component({
	selector: 'wys-app',
	template: `
    <nav [style.display]="islogin ? 'block' : 'none'">
        <ul>
            <li routerLink="/personnel" routerLinkActive="activity">
                <a>员工</a>
            </li>
            <li routerLink='/purchases' routerLinkActive="activity">
                <a >进货</a>
            </li>
            <li routerLink='/sales' routerLinkActive="activity">
                <a>销售</a>
            </li>
            <li routerLink='/pos' routerLinkActive="activity">
                <a>零售</a>
            </li>
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
	`
})
export class AppComponent implements OnInit {
    username:string;
    islogin:boolean;
    constructor(
        private _staffService:StaffService,
        private router:Router
    ){}

    ngOnInit() {
        console.log(this.username);
        setInterval(()=>{
            let pk = sessionStorage.getItem('user');
            if(pk) {
                this.islogin = true;
                if(typeof(this.username)=="undefined") {
                    this._staffService.get_user_staff(Number(pk)).subscribe(
                        staff=>{
                            this.username = staff.name;
                        },
                        error=>alert(error)
                    );
                }
            } else {
                this.islogin = false;
            }
        },2000);
    }
 }
