import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home';

export const appRoutes: Routes = [
    { path:'',component:HomeComponent },
    { path:'login',loadChildren: ()=>System.import("./+login")}
];