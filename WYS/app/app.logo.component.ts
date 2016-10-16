import { Component } from '@angular/core';

@Component({
	moduleId: module.id,
	selector: 'wys-logo',
	template: `
        <div class="logo">
            <h1>
                <span style="color:rgb(164,74,140)">s</span>c
            </h1>
            <form action="/department">
                <label for="name">用户名</label>
                <input type="text" id="name" autofocus="autofocus">
                <label for="passwd">密码</label>
                <input type="password" id="passwd">
                <input type="submit" value="登录" class="submit">
            </form>
        </div>
       
    `,
  
})
export class  LogoComponent{

}
