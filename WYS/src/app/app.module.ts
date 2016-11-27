import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { HomeComponent } from './home';

import { appRoutes } from './app.routing';
 
@NgModule({
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    RouterModule.forRoot(appRoutes)
  ],

  declarations: [
    AppComponent,
    HomeComponent
  ],

  providers: [
  ],

  bootstrap: [ 
    AppComponent
  ]
})
export class AppModule { }
