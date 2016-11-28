import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home';
import { AuthGuard } from './auth.guard';

export const appRoutes: Routes = [
    { path:'',canActivate:[ AuthGuard ],loadChildren:()=>System.import('./erp') },
    { path:'login',loadChildren: ()=>System.import("./+login")}
];