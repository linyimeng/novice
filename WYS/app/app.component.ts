import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
	moduleId: module.id,
	selector: 'wys-app',
	template: `
	<wys-nav></wys-nav>
	<router-outlet></router-outlet>
	`
})
export class AppComponent { }
