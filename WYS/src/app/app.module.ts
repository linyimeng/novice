import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';
import { FileUploadModule } from 'ng2-file-upload';
import { AppComponent } from './app.component';

import { appRoutes } from './app.routing';

import { AuthGuard } from './auth.guard';
 
@NgModule({
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    FileUploadModule,
    RouterModule.forRoot(appRoutes)
  ],

  declarations: [
    AppComponent,
  ],

  providers: [
    AuthGuard,
  ],

  bootstrap: [ 
    AppComponent
  ]
})
export class AppModule { }
