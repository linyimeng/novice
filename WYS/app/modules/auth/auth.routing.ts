import { Routes } from '@angular/router';

import { AuthTokenGuard } from './authtoken.guard';
import { LoginComponent } from './login.component';

export const loginRoutes:Routes = [
    { path:'login', component:LoginComponent }
];

export const authtokenProviders = [
    AuthTokenGuard,
];