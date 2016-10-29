import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   
   selector: 'department-right',
   templateUrl: 'department-right.html'

})
export class DepartmentrightComponent {
    is_show_create = false;
    show_or_hidden_create() {
        if(this.is_show_create) {
            this.is_show_create = false;
        } else {
            this.is_show_create = true;
        }
    }

    
}

