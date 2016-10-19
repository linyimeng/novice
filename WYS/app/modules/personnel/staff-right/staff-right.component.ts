import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
   moduleId: module.id,
   selector: 'staff-right',
   templateUrl: 'staff-right.html'
})
export class StaffrightComponent {
    constructor(
        private router:Router
    ) {}

    showstaffcreate() {
        this.router.navigate(['/staff/create']);
    }
}

