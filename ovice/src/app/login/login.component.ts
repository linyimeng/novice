import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { AuthService } from '../services/auth.service';


export class Login {
	constructor(
		public username:string,
		public password:string
	){}
}

@Component({
	selector: 'login',
	templateUrl:'login.html',
	styleUrls:['login.css'],
	providers:[ AuthService ]
})
export class LoginComponent {
	login:Login = new Login(null,null);

	constructor(
		private _authService:AuthService,
		private router:Router
	) { }

	loginx(){
		let json = JSON.stringify(this.login);
		console.log(json);
		this._authService.get_auth_token(json).subscribe(
			user=>{
				sessionStorage.setItem('wystoken',user.auth_token);
				sessionStorage.setItem('user',user.user);
				sessionStorage.setItem('eid',user.eid);
				setTimeout(()=>{
					this.router.navigate(['/']);
				},800);
			},
			error=>alert(error)
		);
	}

}
